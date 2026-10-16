"""Prepare exact platform payloads from Lean-reported declaration spans.

The final proof inlines the pinned canonical upstream modules without changing
their declarations, shares the platform's original problem definitions, and
imports the two new, genuinely used intermediate theorems.
"""
from pathlib import Path
import json,re
ROOT=Path(__file__).parent
OUT=ROOT/'Platform';OUT.mkdir(exist_ok=True)

def facts(name):
 return [json.loads(s) for s in (ROOT/'Verification'/f'{name}.facts.jsonl').read_text(encoding='utf8').splitlines() if s.startswith('{') and json.loads(s).get('kind')=='decl']
def raw(name):return (ROOT/'AverageSensitivity'/f'{name}.lean').read_bytes()
def decl(name,target,header=False):
 row=next(r for r in facts(name) if r['nameText']==target)
 data=raw(name);a=row['declStart']['offset'];b=row['valStart']['offset'] if header else row['declEnd']['offset']
 return data[a:b].decode('utf8')
def body(path):return re.sub(r'^import [^\n]+\n','',path.read_text(encoding='utf8'),flags=re.M)
def without(name,targets):
 data=raw(name)
 for r in sorted([r for r in facts(name) if r['nameText'] in targets],key=lambda r:r['declStart']['offset'],reverse=True):
  data=data[:r['declStart']['offset']]+data[r['declEnd']['offset']:]
 return re.sub(r'^import [^\n]+\n','',data.decode('utf8'),flags=re.M)
def imports(paths):return sorted(set(m for p in paths for m in re.findall(r'^import (Mathlib[^\s]+)',p.read_text(encoding='utf8'),re.M)))
baseimport='import Mathlib\n'
data_defs='import Mathlib.Data.Nat.Choose.Central\nimport Mathlib.Algebra.BigOperators.Ring.Finset\nimport Mathlib.Data.Real.Basic\n\nopen scoped BigOperators\nnamespace AverageSensitivity\n\n'+'\n\n'.join(decl('BinomialMAD',n) for n in ['rawMAD','central','mad'])+'\n\nend AverageSensitivity\n'
(OUT/'constants_definition.lean').write_text(data_defs,encoding='utf8')
(ROOT/'Definitions/Def_AverageSensitivity_Constants3762.lean').write_text(data_defs,encoding='utf8')

nodes=[('finite_coupling_refined','RefinedCoupling'),('extract_constant','ConstantExtraction'),('polynomial_bound_3762_general','Multilinearization')]
metadata=[]
for name,mod in nodes:
 header=decl(mod,name,True)
 statement=header.replace('theorem '+name,'theorem AverageSensitivity.'+name,1)+':= by sorry\n'
 preamble='import Mathlib\n'
 if name=='extract_constant':preamble+='import Definitions.Def_AverageSensitivity_Constants3762\n'
 if name=='polynomial_bound_3762_general':preamble+='import Definitions.Def_GotsmanLinial\nopen OAI.LeanBlast.GotsmanLinial\n'
 preamble+='open scoped BigOperators\nopen AverageSensitivity\n' if name=='extract_constant' else 'open scoped BigOperators\n'
 (OUT/(name+'_statement.lean.txt')).write_text(preamble+'\n'+statement,encoding='utf8')
 metadata.append({'name':name,'module':mod,'theorem_name':'AverageSensitivity.'+name,'preamble':preamble,'formal_statement':statement})

scalar=ROOT/'OAI/Combinatorics/GotsmanLinial/ScalarIncrements.lean'
finite=baseimport+'\n'+body(scalar)+'\n'+body(ROOT/'AverageSensitivity/RefinedCoupling.lean')
finite+='\ntheorem solution : type_of% @AverageSensitivity.finite_coupling_refined := @AverageSensitivity.finite_coupling_refined\n'
(OUT/'finite_coupling_refined_solution.lean').write_text(finite,encoding='utf8')

constants='import Mathlib\nimport Definitions.Def_AverageSensitivity_Constants3762\n\n'+without('BinomialMAD',{'rawMAD','central','mad'})+'\n'+body(ROOT/'AverageSensitivity/ConstantExtraction.lean')
constants+='\ntheorem solution : type_of% @AverageSensitivity.extract_constant := @AverageSensitivity.extract_constant\n'
(OUT/'extract_constant_solution.lean').write_text(constants,encoding='utf8')

# Canonical upstream import closure, in topological order. Preserve complete
# module bodies and all namespace/section commands; only project imports go.
seen=set();ordered=[]
def visit(m):
 if m in seen:return
 seen.add(m);p=ROOT/Path(*m.split('.')).with_suffix('.lean')
 for d in re.findall(r'^import (OAI[^\s]+)',p.read_text(encoding='utf8'),re.M):visit(d)
 ordered.append(p)
visit('OAI.Combinatorics.GotsmanLinial.Main')
main='import Mathlib\nimport Definitions.Def_GotsmanLinial\nimport Theorems.Thm_AverageSensitivity_finite_coupling_refined\nimport Theorems.Thm_AverageSensitivity_extract_constant\n\n'
# Model's primitives are exactly those in the platform's pinned Def_GotsmanLinial.
# The only additional Model declaration is this ordered-edge count definition.
main+='namespace OAI.LeanBlast.GotsmanLinial\nopen scoped BigOperators\nnoncomputable def sensitiveEdgeCount {n : ℕ} (f : Cube n → ℝ) : ℕ :=\n  ∑ i : Fin n, (sensitiveVertices f i).card\nend OAI.LeanBlast.GotsmanLinial\n\n'
for p in ordered:
 if p.name=='Model.lean':continue
 main+='\n-- Canonical upstream module: '+str(p.relative_to(ROOT))+'\n'+body(p)+'\n'
for mod in ['BlockRefinement','PolynomialBound','Multilinearization']:
 main+='\n-- Refinement module: '+mod+'\n'+body(ROOT/'AverageSensitivity'/f'{mod}.lean')+'\n'
main+='\ntheorem solution : type_of% @AverageSensitivity.polynomial_bound_3762_general := @AverageSensitivity.polynomial_bound_3762_general\n'
(OUT/'polynomial_bound_3762_general_solution.lean').write_text(main,encoding='utf8')
(OUT/'payload_headers.json').write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
for v in metadata:
 (ROOT/'Theorems'/('Thm_'+v['theorem_name'].replace('.','_')+'.lean')).write_text(v['preamble']+'\n'+v['formal_statement'],encoding='utf8')
print('Prepared',len(metadata),'theorem payloads; final solution',len(main.encode()),'bytes')

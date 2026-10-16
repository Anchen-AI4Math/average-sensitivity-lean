"""Check the saved live proposal against the accepted proof graph."""
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
verification = root / 'Verification'

def read(name):
    return json.loads((verification / name).read_text(encoding='utf8'))

proposal = read('mission_proposal.json')
milestones = read('mission_milestones.json')['milestones']
proof = read('final_audit.json')
structure = json.loads((root / 'Platform/mission_structure.json').read_text(encoding='utf8'))
assert proposal['id'] == 'f1d5911a-0f78-458d-a466-efe14879e460'
assert proposal['status'] == 'Draft'
assert proposal['visibility'] == 'public'
assert proposal['mission_id'] is None
assert proposal['mission_type'] == 'ResearchPaper'
assert len(proposal['fields']) == 2
assert proposal['main_item_id'] == structure['main_item_id']
assert proposal['item_order'] == structure['item_order']
items = proposal['items']
assert [i['id'] for i in items] == structure['item_order']
assert len(items) == 5 and all(i['kind'] == 'reference' for i in items)
assert [i['status'] for i in items] == ['Definition', 'Definition', 'Proved', 'Proved', 'Proved']
assert [i['role'] for i in items] == [None, None, 'milestone', 'milestone', 'goal']
assert all(i['confirmed_at'] is None for i in items)
assert len(milestones) == 2
assert [m['item_id'] for m in milestones] == [i['id'] for i in items[2:4]]
assert [m['theorem_id'] for m in milestones] == proof['supporting_theorems']
assert items[-1]['theorem_id'] == proof['root']
assert proof['root_status'] == 'Proved' and proof['open_nodes'] == 0
for milestone in milestones:
    assert any(path[0] == milestone['theorem_id'] and path[-1] == proof['root']
               for path in proof['verified_paths'])

record = {
    'checked_at': datetime.now(timezone.utc).isoformat(),
    'proposal_id': proposal['id'],
    'name': proposal['name'],
    'status': proposal['status'],
    'intended_visibility': proposal['visibility'],
    'live_mission_id': proposal['mission_id'],
    'main_theorem': proof['root'],
    'ordered_items': [{k:i[k] for k in ('id', 'theorem_id', 'theorem_name', 'role', 'status')}
                      for i in items],
    'milestone_count': len(milestones),
    'all_items_reference_existing_nodes': True,
    'both_milestones_are_actual_goal_dependencies': True,
    'all_theorem_nodes_proved': True,
    'open_proof_nodes': proof['open_nodes'],
    'human_confirmations_performed_by_agent': False,
    'remaining_step': 'Human owner confirms the five items and clicks Submit Proposal; moderator approval makes the mission live.',
    'review_entry': 'https://prove2.me/my-missions',
}
(verification / 'mission_audit.json').write_text(
    json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf8')
print(json.dumps(record, ensure_ascii=True, indent=2))

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'labs'/'scripts'))
from validate_fixture import rows,validate_data
from evaluate_retrieval import precision_recall

class FixtureTests(unittest.TestCase):
    def setUp(self):
        d=ROOT/'labs'/'data'
        self.tables=[rows(d/n) for n in ['accounts.csv','customers.csv','account_memberships.csv','service_requests.csv']]

    def test_valid_data(self):
        self.assertEqual(validate_data(*self.tables),[])

    def test_duplicate_account_rejected(self):
        accounts,customers,members,requests=copy.deepcopy(self.tables)
        accounts.append(dict(accounts[0]))
        self.assertTrue(any('duplicate key' in e for e in validate_data(accounts,customers,members,requests)))

    def test_cross_account_orphan_rejected(self):
        accounts,customers,members,requests=copy.deepcopy(self.tables)
        requests[0]['account_id']='A-DOES-NOT-EXIST'
        self.assertTrue(any('orphan account' in e for e in validate_data(accounts,customers,members,requests)))

    def test_invalid_status_rejected(self):
        accounts,customers,members,requests=copy.deepcopy(self.tables)
        requests[0]['status']='BANANA'
        self.assertTrue(any('invalid status' in e for e in validate_data(accounts,customers,members,requests)))

    def test_retrieval_precision_recall(self):
        p,r=precision_recall(['P01','P02','P03'],['P02','P09','P03'],3)
        self.assertAlmostEqual(p,2/3)
        self.assertAlmostEqual(r,2/3)

    def test_retrieval_no_answer(self):
        self.assertEqual(precision_recall([],[],3),(1.0,1.0))
        self.assertEqual(precision_recall([],['P05'],3),(0.0,0.0))

    def test_golden_evidence_ids_valid(self):
        docs=json.loads((ROOT/'labs/data/approved_policies.json').read_text())
        allowed={p['passage_id'] for p in docs if p['audience']=='CUSTOMER' and p['version']>=2}
        qs=json.loads((ROOT/'labs/evaluation/golden_questions.json').read_text())
        for q in qs:
            self.assertTrue(set(q['retrieved_passage_ids']).issubset(allowed),q['id'])
            self.assertTrue(set(q['must_cite']).issubset(set(q['relevant_passage_ids'])),q['id'])

if __name__=='__main__':unittest.main()

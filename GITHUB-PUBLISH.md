# Publish this repository to GitHub

This ZIP is **ready for a public content review**, but it does not publish itself and has no live Salesforce dependencies. Review [`PUBLISHING-CHECKLIST.md`](PUBLISHING-CHECKLIST.md) before making it public.

## New repository (recommended)

1. Create a new repository called `Salesforce-Data360-Agentforce-Architecture-Playbook` under your GitHub account. Keep it private during final review, then choose public.
2. Unzip this archive into a local folder. Open a terminal in the folder (next to `README.md`).
3. Run the checks and push:

```bash
python3 labs/scripts/validate_fixture.py
python3 -m unittest discover -s tests -v
python3 labs/scripts/check_content.py
git init
git branch -M main
git add .
git commit -m "Publish independent Data 360 and Agentforce architecture playbook"
git remote add origin https://github.com/YOUR_USERNAME/Salesforce-Data360-Agentforce-Architecture-Playbook.git
git push -u origin main
```

If the GitHub repo was created with a README or license, clone it first and copy the package content into it; avoid overwriting unrelated commits.

4. Verify links/diagrams render and Actions checks pass. Add a short repo description, topics `salesforce`, `data360`, `agentforce`, `rag`, `architecture`, `snowflake`, `solution-design`, and link a real public URL into `social/linkedin-series.md` before posting.
5. Publish/schedule LinkedIn posts only after the repository is publicly accessible and the content is reviewed.

**Existing project coexistence:** This is a documentation-first architecture playbook. You may link it from your separate pre-existing Salesforce DX learning project; do not overwrite its Salesforce metadata or claim these examples were deployed there.

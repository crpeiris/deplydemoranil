# Git Practice Exercises

These short exercises will help teams use Git effectively while working on the project.

1) Initialize and push

  - git init
  - git add .
  - git commit -m "Initial commit"
  - git branch -M main
  - git remote add origin <your-remote-url>
  - git push -u origin main

2) Feature branch workflow

  - git checkout -b feature/login
  - work on feature
  - git add . && git commit -m "Add login view"
  - git push origin feature/login
  - open a Pull Request and merge via the web UI

3) Collaborative workflow

  - Pull changes frequently: git pull --rebase
  - Resolve conflicts locally, then test and push

4) Good commit messages

  - Use present tense: "Add user login"
  - Keep them concise and informative

5) Small tips

  - Use .gitignore to avoid committing environment files
  - Protect main branch with branch protection rules in your repo

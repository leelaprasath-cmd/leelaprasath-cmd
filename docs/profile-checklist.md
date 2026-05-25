# Profile Optimization & Maintenance Checklist

Follow this checklist to initialize, configure, and maintain an elite systems engineering profile on GitHub.

---

## 🛠️ Step 1: Initializing Your Profile Repository
1. **Create Repository**: Create a public repository named exactly matching your username: `leelaprasath-cmd`.
2. **Initialize**: Check the box to initialize it with a `README.md`.
3. **Branch Setup**:
   - Make sure your primary default branch is named `main`.
   - Create an empty orphan branch named `github-pages` to store the generated snake game animation asset:
     ```bash
     git checkout --orphan github-pages
     git rm -rf .
     git commit --allow-empty -m "Initial commit for pages telemetry"
     git push origin github-pages
     git checkout main
     ```

---

## 📁 Step 2: Uploading Deliverables
Copy and paste the files we generated into your local clones:
- **`README.md`**: Place it in the root of your `leelaprasath-cmd/leelaprasath-cmd` repository.
- **`assets/typing.svg`**: Create an `assets/` folder in the root and place the `typing.svg` file inside.
- **`.github/workflows/snake.yml`**: Create the nested folders `.github/workflows/` and save `snake.yml` inside.

*Note: Once you push the workflow on `main`, navigate to the **Actions** tab on GitHub, select the `generate animation` workflow, and click **Run workflow** manually to verify it successfully builds and pushes the snake SVG.*

---

## 📌 Step 3: Pinning Strategy
GitHub allows you to pin up to 6 repositories to the top of your profile. Arrange them in order of complexity and alignment with your goals:

1. **`backend-engineering`** (Top Left): Represents high-level software integration and networking logic.
2. **`system-design-notes`** (Top Middle): Represents architectural systems thinking.
3. **`ml-foundations`** (Top Right): Connects systems with AI principles.
4. **`dsa-python`** (Bottom Left): Demonstrates problem-solving rigor.
5. **`python-foundations`** (Bottom Middle): Represents standard language mastery.
6. **`roadmap-notes`** (Bottom Right): Serves as your structured academic hub.

---

## ⏳ Step 4: Long-Term Growth & Commit Habits
To establish a credible systems engineer profile, adopt these professional commit rules:
- **Write Good Commits**: Use conventional commits (e.g., `feat(hash): implement hash collision unit tests`). Avoid vague messages like `update code` or `fixed bugs`.
- **Maintain a Clean Grid**: Focus on high-quality commits on 3-5 days per week. Avoid using automated fake green-grid script tools, as experienced engineers spot them immediately.
- **Keep it Transparent**: Keep learning repositories public. Every commit shows your active work on a specific day, demonstrating discipline.
- **Document Progress**: After completing each roadmap stage, update the progress bar inside your `README.md` (e.g., change `Phase 1: [██░░░░░░░░░░░░░░░░░░]` to show higher percentages).

---

## 🧼 Step 5: Profile Cleanup Rules
- **No Cringe Hype**: Avoid titles like "AI wizard" or "Generative AI Guru" when starting out. Use grounded terms like "Future Systems Engineer" or "Distributed Systems Learner."
- **Clean Avatar**: Use a high-quality professional portrait or a clean minimal developer avatar/logo.
- **Minimal Bio**: Keep the GitHub bio short and direct:
  > *BE CSE Student | Learning distributed systems, backend architectures, and agentic infrastructure.*
- **Clean Up Old Repositories**: Archive or delete old high school projects or unused test repositories to keep your profile focused.

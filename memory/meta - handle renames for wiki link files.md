### Handle File Renames

wiki links break when names change. always use this workflow:


# step 1: rename with git
git mv "01_thinking/notes/old name.md" "01_thinking/notes/new name.md"

# step 2: update all wiki links
find . -name "*.md" -not -path "./.git/*" -exec sed -i '' \
  's|\[\[old name\]\]|[[new name]]|g' {} \;

# step 3: verify no broken links
grep -r '\[\[old name\]\]' . --include="*.md"
# must return nothing
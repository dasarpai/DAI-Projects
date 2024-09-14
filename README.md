# 1-Dasarpai-Projects


# To track large files on github
Used following command in this folder.

git lfs install 
 
# Used following command to track models
git lfs track *.pth

# If want to commit from command prompt (other use desktop)
Commit the .gitattributes file: When you run git lfs track, it updates a file called .gitattributes with the file types being tracked. You need to commit this file to your repository so that others (and GitHub) know to use LFS for these file types.

git add .gitattributes
git commit -m "Add .gitattributes for LFS tracking"

# Push your changes to GitHub: Once your files are tracked and committed, push your changes to the repository using GitHub Desktop or the command line:

git push origin main


# Verify large files are being tracked: You can verify that large files are being handled by Git LFS with the following command:

git lfs ls-files






# cpsc_476_face_ai_02

python3 -m venv .venv

#Step 5: Activate and use the environment
source .venv/bin/activate

pip install --upgrade pip
python -m pip install opencv-python mediapipe cvzone
python CornerRectangleExample.py

pip install djitellopy
python -m python tellopy.py

#certificate installer fix
open "/Applications/Python 3.11/Install Certificates.command"

#error with mediapipe
python -m pip install --force-reinstall "mediapipe==0.10.21"

#numpy issue
python -m pip uninstall opencv-python
python -m pip install "numpy==1.26.4" "opencv-contrib-python==4.11.0.86" "mediapipe==0.10.21"

#try again
python -m pip uninstall -y opencv-python opencv-contrib-python opencv-python-headless opencv-contrib-python-headless
python -m pip install --no-cache-dir "numpy==1.26.4" "opencv-contrib-python==4.11.0.86"

#check if it worked
python -c "import cv2; print(cv2.__version__, cv2.__file__); print(cv2.RETR_EXTERNAL, cv2.VideoCapture)"

#use control+C to quit
python FaceDetectionExample.py

#Steps to create pull request to fix a problem
On GitHub, open cvzone/cvzone and click Fork.

In your terminal, create a branch and set up your fork as the push remote. Replace YOUR-USERNAME with your GitHub username

#Assuming you are on master, you create another branch.  It can be called anything like fix/cross-platform-camera-example
git switch -c fix/cross-platform-camera-example

git remote rename origin upstream
#Since I forked the original source and put it in my new repository, this can be done.
git remote add origin https://github.com/YOUR-USERNAME/cvzone.git

#Stage only the example and README changes. There’s also a modified .gitignore in your worktree; leave it unstaged unless you intend to include it.

git add Examples/CornerRectangleExample.py README.md
git diff --cached

#Review the staged diff to make sure it contains only the changes you want to propose.

#Commit and push the branch

git commit -m "Make corner rectangle example camera selection portable" \
  -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
git push -u origin fix/cross-platform-camera-example


#On GitHub, open your fork. GitHub should offer Compare & pull request. Set the base repository to cvzone/cvzone and the base branch to master, then describe the camera-index detection and frame checks before creating the PR.

#The proposed changes are in CornerRectangleExample.py and README.md.
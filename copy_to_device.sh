DEVICE=/Volumes/CIRCUITPY/
FILES=("code.py")
LIB_FILES=(
  "colors.py"
  "models.py"
  "renderer.py"
  "animations.py"
  "utils.py"
)
echo "Copying $LIB_FILES from src/ to device lib/"
cd src
cp $LIB_FILES $DEVICE/lib

echo "Copying $FILES to device root"
cp $FILES $DEVICE

echo "Syncing filesystem"
sync

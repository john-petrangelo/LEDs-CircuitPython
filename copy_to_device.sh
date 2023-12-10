DEVICE=/Volumes/CIRCUITPY/
FILES=("code.py")
LIB_FILES=("colors.py" "roving_dot.py" "models.py" "renderer.py")
echo "Copying $LIB_FILES to device lib"
cp src/$LIB_FILES $DEVICE/lib

echo "Copying $FILES to device root"
cp src/$FILES $DEVICE

echo "Syncing filesystem"
sync

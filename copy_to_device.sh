DEVICE=/Volumes/CIRCUITPY/

echo "Copying luminaria/ from src/ to device lib/"
cp -R src/luminaria $DEVICE/lib/

echo "Copying examples/ from src/ to device lib/"
cp -R src/examples $DEVICE/lib/

echo "Copying main program to device root"
cp src/code.py $DEVICE

echo "Syncing filesystem"
sync

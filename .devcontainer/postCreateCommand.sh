chmod -R 777 /workspaces/FoodSAM
setfacl -R -d -m u::rwx,g::rwx,o::rwx /workspaces/FoodSAM

# Create and activate huhu environment
conda create -y -q -n foodsam python=3.7

echo "postCreateCommand.sh COMPLETE!"
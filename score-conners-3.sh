source /home/faird/shared/code/external/envs/miniconda3/load_miniconda3.sh
conda activate nibabel_env
export PYTHONPATH=$PYTHONPATH:./src

python ./src/main.py --parents_file_name $1 --age $2 --sex $3

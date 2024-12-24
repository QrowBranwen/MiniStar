env="StarCraft2sp"
map="10sp_protoss"
algo="rmappo"
units="10v10"

exp="tune2"
seed_max=1

echo "env is ${env}, map is ${map}, algo is ${algo}, exp is ${exp}, max seed is ${seed_max}"
for seed in `seq ${seed_max}`;
do
    echo "seed is ${seed}:"
    CUDA_VISIBLE_DEVICES=0 python3 train_smac.py --env_name ${env} --algorithm_name ${algo} --experiment_name ${exp} \
    --map_name ${map} --seed ${seed} --units ${units} --n_training_threads 1 --n_rollout_threads 8 --n_eval_rollout_threads 2 --num_mini_batch 1 --episode_length 400 \
    --num_env_steps 20000000 --ppo_epoch 5 --use_value_active_masks --use_eval --eval_episodes 32 --use_wandb
done

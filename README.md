# MiniStar

MiniStar is an open-source environment built on top of **SMACv2**, designed to support self-play for StarCraft II agents.

## Features
- **Self-Play Environment**: Built to facilitate self-play strategies for agent training.
- **SMACv2 Compatibility**: Extends the popular SMACv2 framework.
- **Integration with OnPolicy**: Utilizes the [OnPolicy](https://github.com/marlbenchmark/onpolicy) project for testing and evaluation.

---

## Getting Started
Follow these steps to set up and use the MiniStar environment:

### 1. Prerequisites
Ensure you have the following installed:
- Python 3.6 or higher
- StarCraft II (SC2) installed 
- SMACv2 installed

### 2. Map Setup
Copy the maps provided in the `sp_maps` directory into your StarCraft II installation:

```bash
cp  sp_maps/* $SC2PATH/Maps/Smac_Maps/
```
Here, `$SC2PATH` refers to the root directory of your StarCraft II installation.

### 3. Update `smac_maps.py`
Use the `smac_maps.py` file to update the SMACv2 map list. Replace the file in your SMACv2 environment with the updated version:

```bash
cp smac_maps.py $smacv2PATH/smacv2/env/starcraft2/maps/smac_maps.py
```
Here, `$smacv2PATH` refers to the root directory of your smacv2 installation.

### 4. Running the Training Script
Start the training script to train a Protoss 10v10 self-play environment:

```bash
sh train_protoss_10v10_selfplay.sh
```

### 5. Testing with OnPolicy
MiniStar leverages the [OnPolicy](https://github.com/marlbenchmark/onpolicy) framework for testing. To test the environment using OnPolicy:

---


---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve MiniStar.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments
- **SMACv2**: The foundation for this environment.
- **StarCraft II**: The platform for agent training.
- **OnPolicy**: Used as the testing framework for this project.

For further questions or support, please open an issue or contact the maintainers.


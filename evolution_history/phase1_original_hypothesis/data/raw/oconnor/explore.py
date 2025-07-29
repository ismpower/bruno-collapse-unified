import h5py

file_path = r"D:\Bruno_Entropy_Project\data\raw\oconnor\NuLib_LS180_noweak_epkernels_rho82_temp65_ye51_ng18_ns3_Itemp65_Ieta61_version1.0_20141111.h5"

with h5py.File(file_path, "r") as f:
    def walk(name, obj):
        if isinstance(obj, h5py.Dataset):
            print(f"📄 {name} → shape: {obj.shape}")
        elif isinstance(obj, h5py.Group):
            print(f"📁 {name}/")
    f.visititems(walk)


import argostranslate.package
import argostranslate.settings

# This setting is sometimes needed on certain networks
argostranslate.settings.https_verify = False

print("Updating the list of available language packages...")
# Step 1: Update the package index
argostranslate.package.update_package_index()

print("Finding and installing required language packages...")
# Get the list of all available packages
available_packages = argostranslate.package.get_available_packages()

# Define the language pairs we need
required_pairs = [('en', 'hi'), ('hi', 'en'), ('en', 'te'), ('te', 'en'), ('en', 'kn'), ('kn', 'en')]

# Step 2: Find and install each required package
for from_code, to_code in required_pairs:
    print(f"  -> Looking for package to translate from '{from_code}' to '{to_code}'...")
    # Filter the list to find the package we want
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        ),
        None
    )
    if package_to_install:
        package_to_install.install()
        print(f"     ✅ Successfully installed.")
    else:
        print(f"     ❌ Package not found.")

print("\nTranslation setup complete.")
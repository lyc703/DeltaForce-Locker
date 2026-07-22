# safe_runner.py
# A safe wrapper to run main.main() without requesting admin or launching Lockhead.exe.
# Use this to check config loading and message decoding without running the installer.

import main

# Override the imported run_as_admin and run_installer names in the main module
# so main.main() will not prompt for UAC or execute the EXE.
main.run_as_admin = lambda: None
main.run_installer = lambda: True

if __name__ == "__main__":
    # Call main.main() which will now show the GUI dialogs but won't elevate or run the EXE.
    # If you want to avoid GUI dialogs too, comment the line below and use the helper script show_messages.py instead.
    main.main()

# Capture and detection configuration
# This YAML-like block is included here based on the user's provided configuration.
# If you prefer it as a separate config file, say so and I will create Desktop/safe_runner_config.yaml.
capture:
  source: "window"
  window_name: "DeltaForce"
  fps: 30
  capture_region: [0,0,1920,1080]
detection:
  model: "models/best.pt"
  conf_threshold: 0.5
  iou_threshold: 0.45
  device: "cpu"
  imgsz: 640 
mouse:
  enable: true
  sensitivity: 0.7
  smooth: true
  max_offset: 300
  button: "left" 
advanced:
  dynamic_path: false
  log_level: "INFO"
  overlay: false

     ] Logs for pose-detection-app-o7zvwgeiuvho4qccmmlfsh.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

[17:56:53] 🖥 Provisioning machine...

[17:56:53] 🎛 Preparing system...

[17:56:53] ⛓ Spinning up manager process...

[17:38:19] 🚀 Starting up repository: 'pose-detection-app', branch: 'main', main module: 'app.py'

[17:38:19] 🐙 Cloning repository...

[17:38:19] 🐙 Cloning into '/mount/src/pose-detection-app'...

[17:38:20] 🐙 Cloned repository!

[17:38:20] 🐙 Pulling code changes from Github...

[17:38:20] 📦 Processing dependencies...

[17:38:20] 📦 Apt dependencies were installed from /mount/src/pose-detection-app/packages.txt using apt-get.

Get:1 http://deb.debian.org/debian-security bullseye-security InRelease [27.2 kB]

Hit:2 http://deb.debian.org/debian trixie InRelease

Get:3 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]

Get:4 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]

Get:5 http://deb.debian.org/debian-security bullseye-security/main amd64 Packages [464 kB]

Get:6 https://packages.microsoft.com/debian/11/prod bullseye InRelease [3650 B]

Get:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index [4995 B]

Err:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index

  Need 4750 compressed bytes, but limit is 4412 and original is 4412

Get:8 http://deb.debian.org/debian-security trixie-security/main amd64 Packages [227 kB]

Get:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index [4995 B]

Ign:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index

Get:9 https://packages.microsoft.com/debian/11/prod bullseye/main amd64 Packages [232 kB]

Get:10 http://deb.debian.org/debian trixie-updates/main amd64 Packages [4412 B]

Get:11 https://packages.microsoft.com/debian/11/prod bullseye/main arm64 Packages [86.0 kB]

Fetched 1140 kB in 0s (5130 kB/s)

Reading package lists...[2026-07-22 17:38:21.421489] 

Reading package lists...[2026-07-22 17:38:22.194004] 

Building dependency tree...[2026-07-22 17:38:22.433064] 

Reading state information...[2026-07-22 17:38:22.433386] 

The following additional packages will be installed:

  libdrm-amdgpu1 libdrm-common libdrm-intel1 libdrm2 libelf1t64 libgbm1 libgl1

  libgl1-mesa-dri libglvnd0 libglx-mesa0 libglx0 libllvm19 libpciaccess0

  libsensors-config libsensors5 libvulkan1 libwayland-client0

  libwayland-server0 libx11-xcb1 libxcb-dri3-0 libxcb-glx0 libxcb-present0

  libxcb-randr0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxml2 libxshmfence1

  libxxf86vm1 libz3-4 mesa-libgallium mesa-vulkan-drivers

Suggested packages:

  pciutils lm-sensors

The following NEW packages will be installed:

  libdrm-amdgpu1 libdrm-common libdrm-intel1 libdrm2 libelf1t64 libgbm1 libgl1

  libgl1-mesa-dri libgl1-mesa-glx libglvnd0 libglx-mesa0 libglx0 libllvm19

  libpciaccess0 libsensors-config libsensors5 libvulkan1 libwayland-client0

  libwayland-server0 libx11-xcb1 libxcb-dri3-0 libxcb-glx0 libxcb-present0

  libxcb-randr0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxml2 libxshmfence1

  libxxf86vm1 libz3-4 mesa-libgallium mesa-vulkan-drivers

0 upgraded, 33 newly installed, 0 to remove and 1 not upgraded.

Need to get 61.2 MB of archives.

After this operation, 292 MB of additional disk space will be used.

Get:1 http://deb.debian.org/debian trixie/main amd64 libdrm-common all 2.4.124-2 [8288 B]

Get:2 http://deb.debian.org/debian trixie/main amd64 libdrm2 amd64 2.4.124-2 [39.0 kB]

Get:3 http://deb.debian.org/debian trixie/main amd64 libdrm-amdgpu1 amd64 2.4.124-2 [22.6 kB]

Get:4 http://deb.debian.org/debian trixie/main amd64 libpciaccess0 amd64 0.17-3+b3 [51.9 kB]

Get:5 http://deb.debian.org/debian trixie/main amd64 libdrm-intel1 amd64 2.4.124-2 [64.1 kB]

Get:6 http://deb.debian.org/debian trixie/main amd64 libelf1t64 amd64 0.192-4 [189 kB]

Get:7 http://deb.debian.org/debian trixie/main amd64 libwayland-server0 amd64 1.23.1-3 [34.4 kB]

Get:8 http://deb.debian.org/debian trixie/main amd64 libxml2 amd64 2.12.7+dfsg+really2.9.14-2.1+deb13u3 [700 kB]

Get:9 http://deb.debian.org/debian trixie/main amd64 libz3-4 amd64 4.13.3-1 [8560 kB]

Get:10 http://deb.debian.org/debian trixie/main amd64 libllvm19 amd64 1:19.1.7-3+b1 [26.0 MB]

Get:11 http://deb.debian.org/debian trixie/main amd64 libsensors-config all 1:3.6.2-2 [16.2 kB]

Get:12 http://deb.debian.org/debian trixie/main amd64 libsensors5 amd64 1:3.6.2-2 [37.5 kB]

Get:13 http://deb.debian.org/debian trixie/main amd64 libx11-xcb1 amd64 2:1.8.12-1 [247 kB]

Get:14 http://deb.debian.org/debian trixie/main amd64 libxcb-dri3-0 amd64 1.17.0-2+b1 [107 kB]

Get:15 http://deb.debian.org/debian trixie/main amd64 libxcb-present0 amd64 1.17.0-2+b1 [106 kB]

Get:16 http://deb.debian.org/debian trixie/main amd64 libxcb-randr0 amd64 1.17.0-2+b1 [117 kB]

Get:17 http://deb.debian.org/debian trixie/main amd64 libxcb-sync1 amd64 1.17.0-2+b1 [109 kB]

Get:18 http://deb.debian.org/debian trixie/main amd64 libxcb-xfixes0 amd64 1.17.0-2+b1 [109 kB]

Get:19 http://deb.debian.org/debian trixie/main amd64 libxshmfence1 amd64 1.3.3-1 [10.9 kB]

Get:20 http://deb.debian.org/debian trixie/main amd64 mesa-libgallium amd64 25.0.7-2+deb13u1 [9630 kB]

Get:21 http://deb.debian.org/debian trixie/main amd64 libgbm1 amd64 25.0.7-2+deb13u1 [44.6 kB]

Get:22 http://deb.debian.org/debian trixie/main amd64 libglvnd0 amd64 1.7.0-1+b2 [52.0 kB]

Get:23 http://deb.debian.org/debian trixie/main amd64 libxcb-glx0 amd64 1.17.0-2+b1 [122 kB]

Get:24 http://deb.debian.org/debian trixie/main amd64 libxcb-shm0 amd64 1.17.0-2+b1 [105 kB]

Get:25 http://deb.debian.org/debian trixie/main amd64 libxxf86vm1 amd64 1:1.1.4-1+b4 [19.3 kB]

Get:26 http://deb.debian.org/debian trixie/main amd64 libvulkan1 amd64 1.4.309.0-1 [130 kB]

Get:27 http://deb.debian.org/debian trixie/main amd64 libgl1-mesa-dri amd64 25.0.7-2+deb13u1 [46.2 kB]

Get:28 http://deb.debian.org/debian trixie/main amd64 libglx-mesa0 amd64 25.0.7-2+deb13u1 [143 kB]

Get:29 http://deb.debian.org/debian trixie/main amd64 libglx0 amd64 1.7.0-1+b2 [34.9 kB]

Get:30 http://deb.debian.org/debian trixie/main amd64 libgl1 amd64 1.7.0-1+b2 [89.5 kB]

Get:31 http://deb.debian.org/debian-security bullseye-security/main amd64 libgl1-mesa-glx amd64 20.3.5-1+deb11u1 [51.3 kB]

Get:32 http://deb.debian.org/debian trixie/main amd64 libwayland-client0 amd64 1.23.1-3 [26.8 kB]

Get:33 http://deb.debian.org/debian trixie/main amd64 mesa-vulkan-drivers amd64 25.0.7-2+deb13u1 [14.2 MB]

debconf: unable to initialize frontend: Dialog

debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)

debconf: falling back to frontend: Readline

debconf: unable to initialize frontend: Readline

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Teletype

debconf: unable to initialize frontend: Teletype

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Noninteractive

Fetched 61.2 MB in 1s (108 MB/s)

Selecting previously unselected package libdrm-common.

(Reading database ... 19815 files and directories currently installed.)

Preparing to unpack .../00-libdrm-common_2.4.124-2_all.deb ...

Unpacking libdrm-common (2.4.124-2) ...

Selecting previously unselected package libdrm2:amd64.

Preparing to unpack .../01-libdrm2_2.4.124-2_amd64.deb ...

Unpacking libdrm2:amd64 (2.4.124-2) ...

Selecting previously unselected package libdrm-amdgpu1:amd64.

Preparing to unpack .../02-libdrm-amdgpu1_2.4.124-2_amd64.deb ...

Unpacking libdrm-amdgpu1:amd64 (2.4.124-2) ...

Selecting previously unselected package libpciaccess0:amd64.

Preparing to unpack .../03-libpciaccess0_0.17-3+b3_amd64.deb ...

Unpacking libpciaccess0:amd64 (0.17-3+b3) ...

Selecting previously unselected package libdrm-intel1:amd64.

Preparing to unpack .../04-libdrm-intel1_2.4.124-2_amd64.deb ...

Unpacking libdrm-intel1:amd64 (2.4.124-2) ...

Selecting previously unselected package libelf1t64:amd64.

Preparing to unpack .../05-libelf1t64_0.192-4_amd64.deb ...

Unpacking libelf1t64:amd64 (0.192-4) ...

Selecting previously unselected package libwayland-server0:amd64.

Preparing to unpack .../06-libwayland-server0_1.23.1-3_amd64.deb ...

Unpacking libwayland-server0:amd64 (1.23.1-3) ...

Selecting previously unselected package libxml2:amd64.

Preparing to unpack .../07-libxml2_2.12.7+dfsg+really2.9.14-2.1+deb13u3_amd64.deb ...

Unpacking libxml2:amd64 (2.12.7+dfsg+really2.9.14-2.1+deb13u3) ...

Selecting previously unselected package libz3-4:amd64.

Preparing to unpack .../08-libz3-4_4.13.3-1_amd64.deb ...

Unpacking libz3-4:amd64 (4.13.3-1) ...

Selecting previously unselected package libllvm19:amd64.

Preparing to unpack .../09-libllvm19_1%3a19.1.7-3+b1_amd64.deb ...

Unpacking libllvm19:amd64 (1:19.1.7-3+b1) ...

Selecting previously unselected package libsensors-config.

Preparing to unpack .../10-libsensors-config_1%3a3.6.2-2_all.deb ...

Unpacking libsensors-config (1:3.6.2-2) ...

Selecting previously unselected package libsensors5:amd64.

Preparing to unpack .../11-libsensors5_1%3a3.6.2-2_amd64.deb ...

Unpacking libsensors5:amd64 (1:3.6.2-2) ...

Selecting previously unselected package libx11-xcb1:amd64.

Preparing to unpack .../12-libx11-xcb1_2%3a1.8.12-1_amd64.deb ...

Unpacking libx11-xcb1:amd64 (2:1.8.12-1) ...

Selecting previously unselected package libxcb-dri3-0:amd64.

Preparing to unpack .../13-libxcb-dri3-0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-dri3-0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-present0:amd64.

Preparing to unpack .../14-libxcb-present0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-present0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-randr0:amd64.

Preparing to unpack .../15-libxcb-randr0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-randr0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-sync1:amd64.

Preparing to unpack .../16-libxcb-sync1_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-sync1:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-xfixes0:amd64.

Preparing to unpack .../17-libxcb-xfixes0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-xfixes0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxshmfence1:amd64.

Preparing to unpack .../18-libxshmfence1_1.3.3-1_amd64.deb ...

Unpacking libxshmfence1:amd64 (1.3.3-1) ...

Selecting previously unselected package mesa-libgallium:amd64.

Preparing to unpack .../19-mesa-libgallium_25.0.7-2+deb13u1_amd64.deb ...

Unpacking mesa-libgallium:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libgbm1:amd64.

Preparing to unpack .../20-libgbm1_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libgbm1:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglvnd0:amd64.

Preparing to unpack .../21-libglvnd0_1.7.0-1+b2_amd64.deb ...

Unpacking libglvnd0:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libxcb-glx0:amd64.

Preparing to unpack .../22-libxcb-glx0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-glx0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-shm0:amd64.

Preparing to unpack .../23-libxcb-shm0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-shm0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxxf86vm1:amd64.

Preparing to unpack .../24-libxxf86vm1_1%3a1.1.4-1+b4_amd64.deb ...

Unpacking libxxf86vm1:amd64 (1:1.1.4-1+b4) ...

Selecting previously unselected package libvulkan1:amd64.

Preparing to unpack .../25-libvulkan1_1.4.309.0-1_amd64.deb ...

Unpacking libvulkan1:amd64 (1.4.309.0-1) ...

Selecting previously unselected package libgl1-mesa-dri:amd64.

Preparing to unpack .../26-libgl1-mesa-dri_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libgl1-mesa-dri:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglx-mesa0:amd64.

Preparing to unpack .../27-libglx-mesa0_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libglx-mesa0:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglx0:amd64.

Preparing to unpack .../28-libglx0_1.7.0-1+b2_amd64.deb ...

Unpacking libglx0:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libgl1:amd64.

Preparing to unpack .../29-libgl1_1.7.0-1+b2_amd64.deb ...

Unpacking libgl1:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libgl1-mesa-glx:amd64.

Preparing to unpack .../30-libgl1-mesa-glx_20.3.5-1+deb11u1_amd64.deb ...

Unpacking libgl1-mesa-glx:amd64 (20.3.5-1+deb11u1) ...

Selecting previously unselected package libwayland-client0:amd64.

Preparing to unpack .../31-libwayland-client0_1.23.1-3_amd64.deb ...

Unpacking libwayland-client0:amd64 (1.23.1-3) ...

Selecting previously unselected package mesa-vulkan-drivers:amd64.

Preparing to unpack .../32-mesa-vulkan-drivers_25.0.7-2+deb13u1_amd64.deb ...

Unpacking mesa-vulkan-drivers:amd64 (25.0.7-2+deb13u1) ...

Setting up libxcb-dri3-0:amd64 (1.17.0-2+b1) ...

Setting up libwayland-server0:amd64 (1.23.1-3) ...

Setting up libx11-xcb1:amd64 (2:1.8.12-1) ...

Setting up libpciaccess0:amd64 (0.17-3+b3) ...

Setting up libxcb-xfixes0:amd64 (1.17.0-2+b1) ...

Setting up libglvnd0:amd64 (1.7.0-1+b2) ...

Setting up libxcb-glx0:amd64 (1.17.0-2+b1) ...

Setting up libsensors-config (1:3.6.2-2) ...

Setting up libxcb-shm0:amd64 (1.17.0-2+b1) ...

Setting up libelf1t64:amd64 (0.192-4) ...

Setting up libxxf86vm1:amd64 (1:1.1.4-1+b4) ...

Setting up libxcb-present0:amd64 (1.17.0-2+b1) ...

Setting up libz3-4:amd64 (4.13.3-1) ...

Setting up libxcb-sync1:amd64 (1.17.0-2+b1) ...

Setting up libsensors5:amd64 (1:3.6.2-2) ...

Setting up libvulkan1:amd64 (1.4.309.0-1) ...

Setting up libxshmfence1:amd64 (1.3.3-1) ...

Setting up libxcb-randr0:amd64 (1.17.0-2+b1) ...

Setting up libdrm-common (2.4.124-2) ...

Setting up libxml2:amd64 (2.12.7+dfsg+really2.9.14-2.1+deb13u3) ...

Setting up libwayland-client0:amd64 (1.23.1-3) ...

Setting up libllvm19:amd64 (1:19.1.7-3+b1) ...

Setting up libdrm2:amd64 (2.4.124-2) ...

Setting up libdrm-amdgpu1:amd64 (2.4.124-2) ...

Setting up mesa-vulkan-drivers:amd64 (25.0.7-2+deb13u1) ...

Setting up libdrm-intel1:amd64 (2.4.124-2) ...

Setting up mesa-libgallium:amd64 (25.0.7-2+deb13u1) ...

Setting up libgbm1:amd64 (25.0.7-2+deb13u1) ...

Setting up libgl1-mesa-dri:amd64 (25.0.7-2+deb13u1) ...

Setting up libglx-mesa0:amd64 (25.0.7-2+deb13u1) ...

Setting up libglx0:amd64 (1.7.0-1+b2) ...

Setting up libgl1:amd64 (1.7.0-1+b2) ...

Setting up libgl1-mesa-glx:amd64 (20.3.5-1+deb11u1) ...

Processing triggers for libc-bin (2.41-12+deb13u3) ...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.14.6 environment at /home/adminuser/venv

Resolved 67 packages in 715ms

[17:38:19] 🚀 Starting up repository: 'pose-detection-app', branch: 'main', main module: 'app.py'

[17:38:19] 🐙 Cloning repository...

[17:38:19] 🐙 Cloning into '/mount/src/pose-detection-app'...

[17:38:20] 🐙 Cloned repository!

[17:38:20] 🐙 Pulling code changes from Github...

[17:38:20] 📦 Processing dependencies...

[17:38:20] 📦 Apt dependencies were installed from /mount/src/pose-detection-app/packages.txt using apt-get.

Get:1 http://deb.debian.org/debian-security bullseye-security InRelease [27.2 kB]

Hit:2 http://deb.debian.org/debian trixie InRelease

Get:3 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]

Get:4 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]

Get:5 http://deb.debian.org/debian-security bullseye-security/main amd64 Packages [464 kB]

Get:6 https://packages.microsoft.com/debian/11/prod bullseye InRelease [3650 B]

Get:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index [4995 B]

Err:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index

  Need 4750 compressed bytes, but limit is 4412 and original is 4412

Get:8 http://deb.debian.org/debian-security trixie-security/main amd64 Packages [227 kB]

Get:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index [4995 B]

Ign:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index

Get:9 https://packages.microsoft.com/debian/11/prod bullseye/main amd64 Packages [232 kB]

Get:10 http://deb.debian.org/debian trixie-updates/main amd64 Packages [4412 B]

Get:11 https://packages.microsoft.com/debian/11/prod bullseye/main arm64 Packages [86.0 kB]

Fetched 1140 kB in 0s (5130 kB/s)

Reading package lists...[2026-07-22 17:38:21.421489] 

Reading package lists...[2026-07-22 17:38:22.194004] 

Building dependency tree...[2026-07-22 17:38:22.433064] 

Reading state information...[2026-07-22 17:38:22.433386] 

The following additional packages will be installed:

  libdrm-amdgpu1 libdrm-common libdrm-intel1 libdrm2 libelf1t64 libgbm1 libgl1

  libgl1-mesa-dri libglvnd0 libglx-mesa0 libglx0 libllvm19 libpciaccess0

  libsensors-config libsensors5 libvulkan1 libwayland-client0

  libwayland-server0 libx11-xcb1 libxcb-dri3-0 libxcb-glx0 libxcb-present0

  libxcb-randr0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxml2 libxshmfence1

  libxxf86vm1 libz3-4 mesa-libgallium mesa-vulkan-drivers

Suggested packages:

  pciutils lm-sensors

The following NEW packages will be installed:

  libdrm-amdgpu1 libdrm-common libdrm-intel1 libdrm2 libelf1t64 libgbm1 libgl1

  libgl1-mesa-dri libgl1-mesa-glx libglvnd0 libglx-mesa0 libglx0 libllvm19

  libpciaccess0 libsensors-config libsensors5 libvulkan1 libwayland-client0

  libwayland-server0 libx11-xcb1 libxcb-dri3-0 libxcb-glx0 libxcb-present0

  libxcb-randr0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxml2 libxshmfence1

  libxxf86vm1 libz3-4 mesa-libgallium mesa-vulkan-drivers

0 upgraded, 33 newly installed, 0 to remove and 1 not upgraded.

Need to get 61.2 MB of archives.

After this operation, 292 MB of additional disk space will be used.

Get:1 http://deb.debian.org/debian trixie/main amd64 libdrm-common all 2.4.124-2 [8288 B]

Get:2 http://deb.debian.org/debian trixie/main amd64 libdrm2 amd64 2.4.124-2 [39.0 kB]

Get:3 http://deb.debian.org/debian trixie/main amd64 libdrm-amdgpu1 amd64 2.4.124-2 [22.6 kB]

Get:4 http://deb.debian.org/debian trixie/main amd64 libpciaccess0 amd64 0.17-3+b3 [51.9 kB]

Get:5 http://deb.debian.org/debian trixie/main amd64 libdrm-intel1 amd64 2.4.124-2 [64.1 kB]

Get:6 http://deb.debian.org/debian trixie/main amd64 libelf1t64 amd64 0.192-4 [189 kB]

Get:7 http://deb.debian.org/debian trixie/main amd64 libwayland-server0 amd64 1.23.1-3 [34.4 kB]

Get:8 http://deb.debian.org/debian trixie/main amd64 libxml2 amd64 2.12.7+dfsg+really2.9.14-2.1+deb13u3 [700 kB]

Get:9 http://deb.debian.org/debian trixie/main amd64 libz3-4 amd64 4.13.3-1 [8560 kB]

Get:10 http://deb.debian.org/debian trixie/main amd64 libllvm19 amd64 1:19.1.7-3+b1 [26.0 MB]

Get:11 http://deb.debian.org/debian trixie/main amd64 libsensors-config all 1:3.6.2-2 [16.2 kB]

Get:12 http://deb.debian.org/debian trixie/main amd64 libsensors5 amd64 1:3.6.2-2 [37.5 kB]

Get:13 http://deb.debian.org/debian trixie/main amd64 libx11-xcb1 amd64 2:1.8.12-1 [247 kB]

Get:14 http://deb.debian.org/debian trixie/main amd64 libxcb-dri3-0 amd64 1.17.0-2+b1 [107 kB]

Get:15 http://deb.debian.org/debian trixie/main amd64 libxcb-present0 amd64 1.17.0-2+b1 [106 kB]

Get:16 http://deb.debian.org/debian trixie/main amd64 libxcb-randr0 amd64 1.17.0-2+b1 [117 kB]

Get:17 http://deb.debian.org/debian trixie/main amd64 libxcb-sync1 amd64 1.17.0-2+b1 [109 kB]

Get:18 http://deb.debian.org/debian trixie/main amd64 libxcb-xfixes0 amd64 1.17.0-2+b1 [109 kB]

Get:19 http://deb.debian.org/debian trixie/main amd64 libxshmfence1 amd64 1.3.3-1 [10.9 kB]

Get:20 http://deb.debian.org/debian trixie/main amd64 mesa-libgallium amd64 25.0.7-2+deb13u1 [9630 kB]

Get:21 http://deb.debian.org/debian trixie/main amd64 libgbm1 amd64 25.0.7-2+deb13u1 [44.6 kB]

Get:22 http://deb.debian.org/debian trixie/main amd64 libglvnd0 amd64 1.7.0-1+b2 [52.0 kB]

Get:23 http://deb.debian.org/debian trixie/main amd64 libxcb-glx0 amd64 1.17.0-2+b1 [122 kB]

Get:24 http://deb.debian.org/debian trixie/main amd64 libxcb-shm0 amd64 1.17.0-2+b1 [105 kB]

Get:25 http://deb.debian.org/debian trixie/main amd64 libxxf86vm1 amd64 1:1.1.4-1+b4 [19.3 kB]

Get:26 http://deb.debian.org/debian trixie/main amd64 libvulkan1 amd64 1.4.309.0-1 [130 kB]

Get:27 http://deb.debian.org/debian trixie/main amd64 libgl1-mesa-dri amd64 25.0.7-2+deb13u1 [46.2 kB]

Get:28 http://deb.debian.org/debian trixie/main amd64 libglx-mesa0 amd64 25.0.7-2+deb13u1 [143 kB]

Get:29 http://deb.debian.org/debian trixie/main amd64 libglx0 amd64 1.7.0-1+b2 [34.9 kB]

Get:30 http://deb.debian.org/debian trixie/main amd64 libgl1 amd64 1.7.0-1+b2 [89.5 kB]

Get:31 http://deb.debian.org/debian-security bullseye-security/main amd64 libgl1-mesa-glx amd64 20.3.5-1+deb11u1 [51.3 kB]

Get:32 http://deb.debian.org/debian trixie/main amd64 libwayland-client0 amd64 1.23.1-3 [26.8 kB]

Get:33 http://deb.debian.org/debian trixie/main amd64 mesa-vulkan-drivers amd64 25.0.7-2+deb13u1 [14.2 MB]

debconf: unable to initialize frontend: Dialog

debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)

debconf: falling back to frontend: Readline

debconf: unable to initialize frontend: Readline

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Teletype

debconf: unable to initialize frontend: Teletype

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Noninteractive

Fetched 61.2 MB in 1s (108 MB/s)

Selecting previously unselected package libdrm-common.

(Reading database ... 19815 files and directories currently installed.)

Preparing to unpack .../00-libdrm-common_2.4.124-2_all.deb ...

Unpacking libdrm-common (2.4.124-2) ...

Selecting previously unselected package libdrm2:amd64.

Preparing to unpack .../01-libdrm2_2.4.124-2_amd64.deb ...

Unpacking libdrm2:amd64 (2.4.124-2) ...

Selecting previously unselected package libdrm-amdgpu1:amd64.

Preparing to unpack .../02-libdrm-amdgpu1_2.4.124-2_amd64.deb ...

Unpacking libdrm-amdgpu1:amd64 (2.4.124-2) ...

Selecting previously unselected package libpciaccess0:amd64.

Preparing to unpack .../03-libpciaccess0_0.17-3+b3_amd64.deb ...

Unpacking libpciaccess0:amd64 (0.17-3+b3) ...

Selecting previously unselected package libdrm-intel1:amd64.

Preparing to unpack .../04-libdrm-intel1_2.4.124-2_amd64.deb ...

Unpacking libdrm-intel1:amd64 (2.4.124-2) ...

Selecting previously unselected package libelf1t64:amd64.

Preparing to unpack .../05-libelf1t64_0.192-4_amd64.deb ...

Unpacking libelf1t64:amd64 (0.192-4) ...

Selecting previously unselected package libwayland-server0:amd64.

Preparing to unpack .../06-libwayland-server0_1.23.1-3_amd64.deb ...

Unpacking libwayland-server0:amd64 (1.23.1-3) ...

Selecting previously unselected package libxml2:amd64.

Preparing to unpack .../07-libxml2_2.12.7+dfsg+really2.9.14-2.1+deb13u3_amd64.deb ...

Unpacking libxml2:amd64 (2.12.7+dfsg+really2.9.14-2.1+deb13u3) ...

Selecting previously unselected package libz3-4:amd64.

Preparing to unpack .../08-libz3-4_4.13.3-1_amd64.deb ...

Unpacking libz3-4:amd64 (4.13.3-1) ...

Selecting previously unselected package libllvm19:amd64.

Preparing to unpack .../09-libllvm19_1%3a19.1.7-3+b1_amd64.deb ...

Unpacking libllvm19:amd64 (1:19.1.7-3+b1) ...

Selecting previously unselected package libsensors-config.

Preparing to unpack .../10-libsensors-config_1%3a3.6.2-2_all.deb ...

Unpacking libsensors-config (1:3.6.2-2) ...

Selecting previously unselected package libsensors5:amd64.

Preparing to unpack .../11-libsensors5_1%3a3.6.2-2_amd64.deb ...

Unpacking libsensors5:amd64 (1:3.6.2-2) ...

Selecting previously unselected package libx11-xcb1:amd64.

Preparing to unpack .../12-libx11-xcb1_2%3a1.8.12-1_amd64.deb ...

Unpacking libx11-xcb1:amd64 (2:1.8.12-1) ...

Selecting previously unselected package libxcb-dri3-0:amd64.

Preparing to unpack .../13-libxcb-dri3-0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-dri3-0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-present0:amd64.

Preparing to unpack .../14-libxcb-present0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-present0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-randr0:amd64.

Preparing to unpack .../15-libxcb-randr0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-randr0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-sync1:amd64.

Preparing to unpack .../16-libxcb-sync1_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-sync1:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-xfixes0:amd64.

Preparing to unpack .../17-libxcb-xfixes0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-xfixes0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxshmfence1:amd64.

Preparing to unpack .../18-libxshmfence1_1.3.3-1_amd64.deb ...

Unpacking libxshmfence1:amd64 (1.3.3-1) ...

Selecting previously unselected package mesa-libgallium:amd64.

Preparing to unpack .../19-mesa-libgallium_25.0.7-2+deb13u1_amd64.deb ...

Unpacking mesa-libgallium:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libgbm1:amd64.

Preparing to unpack .../20-libgbm1_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libgbm1:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglvnd0:amd64.

Preparing to unpack .../21-libglvnd0_1.7.0-1+b2_amd64.deb ...

Unpacking libglvnd0:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libxcb-glx0:amd64.

Preparing to unpack .../22-libxcb-glx0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-glx0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-shm0:amd64.

Preparing to unpack .../23-libxcb-shm0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-shm0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxxf86vm1:amd64.

Preparing to unpack .../24-libxxf86vm1_1%3a1.1.4-1+b4_amd64.deb ...

Unpacking libxxf86vm1:amd64 (1:1.1.4-1+b4) ...

Selecting previously unselected package libvulkan1:amd64.

Preparing to unpack .../25-libvulkan1_1.4.309.0-1_amd64.deb ...

Unpacking libvulkan1:amd64 (1.4.309.0-1) ...

Selecting previously unselected package libgl1-mesa-dri:amd64.

Preparing to unpack .../26-libgl1-mesa-dri_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libgl1-mesa-dri:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglx-mesa0:amd64.

Preparing to unpack .../27-libglx-mesa0_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libglx-mesa0:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglx0:amd64.

Preparing to unpack .../28-libglx0_1.7.0-1+b2_amd64.deb ...

Unpacking libglx0:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libgl1:amd64.

Preparing to unpack .../29-libgl1_1.7.0-1+b2_amd64.deb ...

Unpacking libgl1:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libgl1-mesa-glx:amd64.

Preparing to unpack .../30-libgl1-mesa-glx_20.3.5-1+deb11u1_amd64.deb ...

Unpacking libgl1-mesa-glx:amd64 (20.3.5-1+deb11u1) ...

Selecting previously unselected package libwayland-client0:amd64.

Preparing to unpack .../31-libwayland-client0_1.23.1-3_amd64.deb ...

Unpacking libwayland-client0:amd64 (1.23.1-3) ...

Selecting previously unselected package mesa-vulkan-drivers:amd64.

Preparing to unpack .../32-mesa-vulkan-drivers_25.0.7-2+deb13u1_amd64.deb ...

Unpacking mesa-vulkan-drivers:amd64 (25.0.7-2+deb13u1) ...

Setting up libxcb-dri3-0:amd64 (1.17.0-2+b1) ...

Setting up libwayland-server0:amd64 (1.23.1-3) ...

Setting up libx11-xcb1:amd64 (2:1.8.12-1) ...

Setting up libpciaccess0:amd64 (0.17-3+b3) ...

Setting up libxcb-xfixes0:amd64 (1.17.0-2+b1) ...

Setting up libglvnd0:amd64 (1.7.0-1+b2) ...

Setting up libxcb-glx0:amd64 (1.17.0-2+b1) ...

Setting up libsensors-config (1:3.6.2-2) ...

Setting up libxcb-shm0:amd64 (1.17.0-2+b1) ...

Setting up libelf1t64:amd64 (0.192-4) ...

Setting up libxxf86vm1:amd64 (1:1.1.4-1+b4) ...

Setting up libxcb-present0:amd64 (1.17.0-2+b1) ...

Setting up libz3-4:amd64 (4.13.3-1) ...

Setting up libxcb-sync1:amd64 (1.17.0-2+b1) ...

Setting up libsensors5:amd64 (1:3.6.2-2) ...

Setting up libvulkan1:amd64 (1.4.309.0-1) ...

Setting up libxshmfence1:amd64 (1.3.3-1) ...

Setting up libxcb-randr0:amd64 (1.17.0-2+b1) ...

Setting up libdrm-common (2.4.124-2) ...

Setting up libxml2:amd64 (2.12.7+dfsg+really2.9.14-2.1+deb13u3) ...

Setting up libwayland-client0:amd64 (1.23.1-3) ...

Setting up libllvm19:amd64 (1:19.1.7-3+b1) ...

Setting up libdrm2:amd64 (2.4.124-2) ...

Setting up libdrm-amdgpu1:amd64 (2.4.124-2) ...

Setting up mesa-vulkan-drivers:amd64 (25.0.7-2+deb13u1) ...

Setting up libdrm-intel1:amd64 (2.4.124-2) ...

Setting up mesa-libgallium:amd64 (25.0.7-2+deb13u1) ...

Setting up libgbm1:amd64 (25.0.7-2+deb13u1) ...

Setting up libgl1-mesa-dri:amd64 (25.0.7-2+deb13u1) ...

Setting up libglx-mesa0:amd64 (25.0.7-2+deb13u1) ...

Setting up libglx0:amd64 (1.7.0-1+b2) ...

Setting up libgl1:amd64 (1.7.0-1+b2) ...

Setting up libgl1-mesa-glx:amd64 (20.3.5-1+deb11u1) ...

Processing triggers for libc-bin (2.41-12+deb13u3) ...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.14.6 environment at /home/adminuser/venv

Resolved 67 packages in 715ms

[17:57:05] 🚀 Starting up repository: 'pose-detection-app', branch: 'main', main module: 'app.py'

[17:57:05] 🐙 Cloning repository...

[17:57:05] 🐙 Cloning into '/mount/src/pose-detection-app'...

[17:57:06] 🐙 Cloned repository!

[17:57:06] 🐙 Pulling code changes from Github...

[17:57:06] 📦 Processing dependencies...

[17:57:06] 📦 Apt dependencies were installed from /mount/src/pose-detection-app/packages.txt using apt-get.

Get:1 http://deb.debian.org/debian-security bullseye-security InRelease [27.2 kB]

Hit:2 http://deb.debian.org/debian trixie InRelease

Get:3 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]

Get:4 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]

Get:5 http://deb.debian.org/debian-security bullseye-security/main amd64 Packages [464 kB]

Get:6 https://packages.microsoft.com/debian/11/prod bullseye InRelease [3650 B]

Get:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index [4995 B]

Err:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index

  Need 4750 compressed bytes, but limit is 4412 and original is 4412

Get:8 http://deb.debian.org/debian-security trixie-security/main amd64 Packages [227 kB]

Get:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index [4995 B]

Ign:7 http://deb.debian.org/debian trixie-updates/main amd64 Packages.diff/Index

Get:9 https://packages.microsoft.com/debian/11/prod bullseye/main arm64 Packages [86.0 kB]

Get:10 http://deb.debian.org/debian trixie-updates/main amd64 Packages [4412 B]

Get:11 https://packages.microsoft.com/debian/11/prod bullseye/main amd64 Packages [232 kB]

Fetched 1140 kB in 0s (5458 kB/s)

Reading package lists...[2026-07-22 17:57:07.300928] 

Reading package lists...[2026-07-22 17:57:08.002314] 

Building dependency tree...[2026-07-22 17:57:08.206504] 

Reading state information...[2026-07-22 17:57:08.206925] 

The following additional packages will be installed:

  libdrm-amdgpu1 libdrm-common libdrm-intel1 libdrm2 libelf1t64 libgbm1 libgl1

  libgl1-mesa-dri libglvnd0 libglx-mesa0 libglx0 libllvm19 libpciaccess0

  libsensors-config libsensors5 libvulkan1 libwayland-client0

  libwayland-server0 libx11-xcb1 libxcb-dri3-0 libxcb-glx0 libxcb-present0

  libxcb-randr0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxml2 libxshmfence1

  libxxf86vm1 libz3-4 mesa-libgallium mesa-vulkan-drivers

Suggested packages:

  pciutils lm-sensors

The following NEW packages will be installed:

  libdrm-amdgpu1 libdrm-common libdrm-intel1 libdrm2 libelf1t64 libgbm1 libgl1

  libgl1-mesa-dri libgl1-mesa-glx libglvnd0 libglx-mesa0 libglx0 libllvm19

  libpciaccess0 libsensors-config libsensors5 libvulkan1 libwayland-client0

  libwayland-server0 libx11-xcb1 libxcb-dri3-0 libxcb-glx0 libxcb-present0

  libxcb-randr0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxml2 libxshmfence1

  libxxf86vm1 libz3-4 mesa-libgallium mesa-vulkan-drivers

0 upgraded, 33 newly installed, 0 to remove and 1 not upgraded.

Need to get 61.2 MB of archives.

After this operation, 292 MB of additional disk space will be used.

Get:1 http://deb.debian.org/debian trixie/main amd64 libdrm-common all 2.4.124-2 [8288 B]

Get:2 http://deb.debian.org/debian trixie/main amd64 libdrm2 amd64 2.4.124-2 [39.0 kB]

Get:3 http://deb.debian.org/debian trixie/main amd64 libdrm-amdgpu1 amd64 2.4.124-2 [22.6 kB]

Get:4 http://deb.debian.org/debian trixie/main amd64 libpciaccess0 amd64 0.17-3+b3 [51.9 kB]

Get:5 http://deb.debian.org/debian trixie/main amd64 libdrm-intel1 amd64 2.4.124-2 [64.1 kB]

Get:6 http://deb.debian.org/debian trixie/main amd64 libelf1t64 amd64 0.192-4 [189 kB]

Get:7 http://deb.debian.org/debian trixie/main amd64 libwayland-server0 amd64 1.23.1-3 [34.4 kB]

Get:8 http://deb.debian.org/debian trixie/main amd64 libxml2 amd64 2.12.7+dfsg+really2.9.14-2.1+deb13u3 [700 kB]

Get:9 http://deb.debian.org/debian trixie/main amd64 libz3-4 amd64 4.13.3-1 [8560 kB]

Get:10 http://deb.debian.org/debian trixie/main amd64 libllvm19 amd64 1:19.1.7-3+b1 [26.0 MB]

Get:11 http://deb.debian.org/debian trixie/main amd64 libsensors-config all 1:3.6.2-2 [16.2 kB]

Get:12 http://deb.debian.org/debian trixie/main amd64 libsensors5 amd64 1:3.6.2-2 [37.5 kB]

Get:13 http://deb.debian.org/debian trixie/main amd64 libx11-xcb1 amd64 2:1.8.12-1 [247 kB]

Get:14 http://deb.debian.org/debian trixie/main amd64 libxcb-dri3-0 amd64 1.17.0-2+b1 [107 kB]

Get:15 http://deb.debian.org/debian trixie/main amd64 libxcb-present0 amd64 1.17.0-2+b1 [106 kB]

Get:16 http://deb.debian.org/debian trixie/main amd64 libxcb-randr0 amd64 1.17.0-2+b1 [117 kB]

Get:17 http://deb.debian.org/debian trixie/main amd64 libxcb-sync1 amd64 1.17.0-2+b1 [109 kB]

Get:18 http://deb.debian.org/debian trixie/main amd64 libxcb-xfixes0 amd64 1.17.0-2+b1 [109 kB]

Get:19 http://deb.debian.org/debian trixie/main amd64 libxshmfence1 amd64 1.3.3-1 [10.9 kB]

Get:20 http://deb.debian.org/debian trixie/main amd64 mesa-libgallium amd64 25.0.7-2+deb13u1 [9630 kB]

Get:21 http://deb.debian.org/debian trixie/main amd64 libgbm1 amd64 25.0.7-2+deb13u1 [44.6 kB]

Get:22 http://deb.debian.org/debian trixie/main amd64 libglvnd0 amd64 1.7.0-1+b2 [52.0 kB]

Get:23 http://deb.debian.org/debian trixie/main amd64 libxcb-glx0 amd64 1.17.0-2+b1 [122 kB]

Get:24 http://deb.debian.org/debian trixie/main amd64 libxcb-shm0 amd64 1.17.0-2+b1 [105 kB]

Get:25 http://deb.debian.org/debian trixie/main amd64 libxxf86vm1 amd64 1:1.1.4-1+b4 [19.3 kB]

Get:26 http://deb.debian.org/debian trixie/main amd64 libvulkan1 amd64 1.4.309.0-1 [130 kB]

Get:27 http://deb.debian.org/debian trixie/main amd64 libgl1-mesa-dri amd64 25.0.7-2+deb13u1 [46.2 kB]

Get:28 http://deb.debian.org/debian trixie/main amd64 libglx-mesa0 amd64 25.0.7-2+deb13u1 [143 kB]

Get:29 http://deb.debian.org/debian trixie/main amd64 libglx0 amd64 1.7.0-1+b2 [34.9 kB]

Get:30 http://deb.debian.org/debian trixie/main amd64 libgl1 amd64 1.7.0-1+b2 [89.5 kB]

Get:31 http://deb.debian.org/debian-security bullseye-security/main amd64 libgl1-mesa-glx amd64 20.3.5-1+deb11u1 [51.3 kB]

Get:32 http://deb.debian.org/debian trixie/main amd64 libwayland-client0 amd64 1.23.1-3 [26.8 kB]

Get:33 http://deb.debian.org/debian trixie/main amd64 mesa-vulkan-drivers amd64 25.0.7-2+deb13u1 [14.2 MB]

debconf: unable to initialize frontend: Dialog

debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)

debconf: falling back to frontend: Readline

debconf: unable to initialize frontend: Readline

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Teletype

debconf: unable to initialize frontend: Teletype

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Noninteractive

Fetched 61.2 MB in 0s (157 MB/s)

Selecting previously unselected package libdrm-common.

(Reading database ... 19815 files and directories currently installed.)

Preparing to unpack .../00-libdrm-common_2.4.124-2_all.deb ...

Unpacking libdrm-common (2.4.124-2) ...

Selecting previously unselected package libdrm2:amd64.

Preparing to unpack .../01-libdrm2_2.4.124-2_amd64.deb ...

Unpacking libdrm2:amd64 (2.4.124-2) ...

Selecting previously unselected package libdrm-amdgpu1:amd64.

Preparing to unpack .../02-libdrm-amdgpu1_2.4.124-2_amd64.deb ...

Unpacking libdrm-amdgpu1:amd64 (2.4.124-2) ...

Selecting previously unselected package libpciaccess0:amd64.

Preparing to unpack .../03-libpciaccess0_0.17-3+b3_amd64.deb ...

Unpacking libpciaccess0:amd64 (0.17-3+b3) ...

Selecting previously unselected package libdrm-intel1:amd64.

Preparing to unpack .../04-libdrm-intel1_2.4.124-2_amd64.deb ...

Unpacking libdrm-intel1:amd64 (2.4.124-2) ...

Selecting previously unselected package libelf1t64:amd64.

Preparing to unpack .../05-libelf1t64_0.192-4_amd64.deb ...

Unpacking libelf1t64:amd64 (0.192-4) ...

Selecting previously unselected package libwayland-server0:amd64.

Preparing to unpack .../06-libwayland-server0_1.23.1-3_amd64.deb ...

Unpacking libwayland-server0:amd64 (1.23.1-3) ...

Selecting previously unselected package libxml2:amd64.

Preparing to unpack .../07-libxml2_2.12.7+dfsg+really2.9.14-2.1+deb13u3_amd64.deb ...

Unpacking libxml2:amd64 (2.12.7+dfsg+really2.9.14-2.1+deb13u3) ...

Selecting previously unselected package libz3-4:amd64.

Preparing to unpack .../08-libz3-4_4.13.3-1_amd64.deb ...

Unpacking libz3-4:amd64 (4.13.3-1) ...

Selecting previously unselected package libllvm19:amd64.

Preparing to unpack .../09-libllvm19_1%3a19.1.7-3+b1_amd64.deb ...

Unpacking libllvm19:amd64 (1:19.1.7-3+b1) ...

Selecting previously unselected package libsensors-config.

Preparing to unpack .../10-libsensors-config_1%3a3.6.2-2_all.deb ...

Unpacking libsensors-config (1:3.6.2-2) ...

Selecting previously unselected package libsensors5:amd64.

Preparing to unpack .../11-libsensors5_1%3a3.6.2-2_amd64.deb ...

Unpacking libsensors5:amd64 (1:3.6.2-2) ...

Selecting previously unselected package libx11-xcb1:amd64.

Preparing to unpack .../12-libx11-xcb1_2%3a1.8.12-1_amd64.deb ...

Unpacking libx11-xcb1:amd64 (2:1.8.12-1) ...

Selecting previously unselected package libxcb-dri3-0:amd64.

Preparing to unpack .../13-libxcb-dri3-0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-dri3-0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-present0:amd64.

Preparing to unpack .../14-libxcb-present0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-present0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-randr0:amd64.

Preparing to unpack .../15-libxcb-randr0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-randr0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-sync1:amd64.

Preparing to unpack .../16-libxcb-sync1_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-sync1:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-xfixes0:amd64.

Preparing to unpack .../17-libxcb-xfixes0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-xfixes0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxshmfence1:amd64.

Preparing to unpack .../18-libxshmfence1_1.3.3-1_amd64.deb ...

Unpacking libxshmfence1:amd64 (1.3.3-1) ...

Selecting previously unselected package mesa-libgallium:amd64.

Preparing to unpack .../19-mesa-libgallium_25.0.7-2+deb13u1_amd64.deb ...

Unpacking mesa-libgallium:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libgbm1:amd64.

Preparing to unpack .../20-libgbm1_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libgbm1:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglvnd0:amd64.

Preparing to unpack .../21-libglvnd0_1.7.0-1+b2_amd64.deb ...

Unpacking libglvnd0:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libxcb-glx0:amd64.

Preparing to unpack .../22-libxcb-glx0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-glx0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxcb-shm0:amd64.

Preparing to unpack .../23-libxcb-shm0_1.17.0-2+b1_amd64.deb ...

Unpacking libxcb-shm0:amd64 (1.17.0-2+b1) ...

Selecting previously unselected package libxxf86vm1:amd64.

Preparing to unpack .../24-libxxf86vm1_1%3a1.1.4-1+b4_amd64.deb ...

Unpacking libxxf86vm1:amd64 (1:1.1.4-1+b4) ...

Selecting previously unselected package libvulkan1:amd64.

Preparing to unpack .../25-libvulkan1_1.4.309.0-1_amd64.deb ...

Unpacking libvulkan1:amd64 (1.4.309.0-1) ...

Selecting previously unselected package libgl1-mesa-dri:amd64.

Preparing to unpack .../26-libgl1-mesa-dri_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libgl1-mesa-dri:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglx-mesa0:amd64.

Preparing to unpack .../27-libglx-mesa0_25.0.7-2+deb13u1_amd64.deb ...

Unpacking libglx-mesa0:amd64 (25.0.7-2+deb13u1) ...

Selecting previously unselected package libglx0:amd64.

Preparing to unpack .../28-libglx0_1.7.0-1+b2_amd64.deb ...

Unpacking libglx0:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libgl1:amd64.

Preparing to unpack .../29-libgl1_1.7.0-1+b2_amd64.deb ...

Unpacking libgl1:amd64 (1.7.0-1+b2) ...

Selecting previously unselected package libgl1-mesa-glx:amd64.

Preparing to unpack .../30-libgl1-mesa-glx_20.3.5-1+deb11u1_amd64.deb ...

Unpacking libgl1-mesa-glx:amd64 (20.3.5-1+deb11u1) ...

Selecting previously unselected package libwayland-client0:amd64.

Preparing to unpack .../31-libwayland-client0_1.23.1-3_amd64.deb ...

Unpacking libwayland-client0:amd64 (1.23.1-3) ...

Selecting previously unselected package mesa-vulkan-drivers:amd64.

Preparing to unpack .../32-mesa-vulkan-drivers_25.0.7-2+deb13u1_amd64.deb ...

Unpacking mesa-vulkan-drivers:amd64 (25.0.7-2+deb13u1) ...

Setting up libxcb-dri3-0:amd64 (1.17.0-2+b1) ...

Setting up libwayland-server0:amd64 (1.23.1-3) ...

Setting up libx11-xcb1:amd64 (2:1.8.12-1) ...

Setting up libpciaccess0:amd64 (0.17-3+b3) ...

Setting up libxcb-xfixes0:amd64 (1.17.0-2+b1) ...

Setting up libglvnd0:amd64 (1.7.0-1+b2) ...

Setting up libxcb-glx0:amd64 (1.17.0-2+b1) ...

Setting up libsensors-config (1:3.6.2-2) ...

Setting up libxcb-shm0:amd64 (1.17.0-2+b1) ...

Setting up libelf1t64:amd64 (0.192-4) ...

Setting up libxxf86vm1:amd64 (1:1.1.4-1+b4) ...

Setting up libxcb-present0:amd64 (1.17.0-2+b1) ...

Setting up libz3-4:amd64 (4.13.3-1) ...

Setting up libxcb-sync1:amd64 (1.17.0-2+b1) ...

Setting up libsensors5:amd64 (1:3.6.2-2) ...

Setting up libvulkan1:amd64 (1.4.309.0-1) ...

Setting up libxshmfence1:amd64 (1.3.3-1) ...

Setting up libxcb-randr0:amd64 (1.17.0-2+b1) ...

Setting up libdrm-common (2.4.124-2) ...

Setting up libxml2:amd64 (2.12.7+dfsg+really2.9.14-2.1+deb13u3) ...

Setting up libwayland-client0:amd64 (1.23.1-3) ...

Setting up libllvm19:amd64 (1:19.1.7-3+b1) ...

Setting up libdrm2:amd64 (2.4.124-2) ...

Setting up libdrm-amdgpu1:amd64 (2.4.124-2) ...

Setting up mesa-vulkan-drivers:amd64 (25.0.7-2+deb13u1) ...

Setting up libdrm-intel1:amd64 (2.4.124-2) ...

Setting up mesa-libgallium:amd64 (25.0.7-2+deb13u1) ...

Setting up libgbm1:amd64 (25.0.7-2+deb13u1) ...

Setting up libgl1-mesa-dri:amd64 (25.0.7-2+deb13u1) ...

Setting up libglx-mesa0:amd64 (25.0.7-2+deb13u1) ...

Setting up libglx0:amd64 (1.7.0-1+b2) ...

Setting up libgl1:amd64 (1.7.0-1+b2) ...

Setting up libgl1-mesa-glx:amd64 (20.3.5-1+deb11u1) ...

Processing triggers for libc-bin (2.41-12+deb13u3) ...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.14.6 environment at /home/adminuser/venv

Resolved 67 packages in 600msimport io
import os
import streamlit as st
import numpy as np
from mediapipe.python.solutions import pose as mp_pose
from mediapipe.python.solutions import pose_connections as mp_pose_connections
from PIL import Image, ImageDraw, ImageFont
import tempfile
import av
import threading
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

# ---------- Page config ----------
st.set_page_config(page_title="Pose Detection & Analysis", layout="wide")

# ---------- Page background ----------
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
  background: linear-gradient(135deg, #8BC34A 0%, #FFEB3B 100%);
}
[data-testid="stHeader"] {
  background: transparent;
}
[data-testid="stSidebar"] {
  background: rgba(255, 255, 255, 0.8);
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# ---------- MediaPipe setup ----------

# ---------- Sidebar ----------
st.sidebar.title("Customization Options")
text_size = st.sidebar.slider("Text Size", 0.5, 3.0, 1.0)
text_thickness = st.sidebar.slider("Text Thickness", 1, 5, 2)
text_color = st.sidebar.color_picker("Text Color", "#0000FF")
circle_radius = st.sidebar.slider("Circle Radius", 1, 10, 2)
line_thickness = st.sidebar.slider("Line Thickness", 1, 5, 2)
circle_color = st.sidebar.color_picker("Circle Color", "#FF5733")
line_color = st.sidebar.color_picker("Line Color", "#FF5733")
width = st.sidebar.slider("Width", 300, 1920, 640)
height = st.sidebar.slider("Height", 300, 1080, 480)


def hex_to_rgb(hex_color):
    return tuple(int(hex_color.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))


def build_cfg():
    return {
        "text_size": text_size,
        "text_thickness": text_thickness,
        "text_rgb": hex_to_rgb(text_color),
        "circle_radius": circle_radius,
        "line_thickness": line_thickness,
        "circle_rgb": hex_to_rgb(circle_color),
        "line_rgb": hex_to_rgb(line_color),
    }


# ---------- Angle / posture helpers ----------
def calc_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    rad = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    ang = np.abs(rad * 180.0 / np.pi)
    return 360 - ang if ang > 180 else ang


def analyze_pose(landmarks):
    lm = mp_pose.PoseLandmark
    info = {}

    def pt(l):
        return [landmarks[l].x, landmarks[l].y]

    l_arm = calc_angle(pt(lm.LEFT_SHOULDER), pt(lm.LEFT_ELBOW), pt(lm.LEFT_WRIST))
    r_arm = calc_angle(pt(lm.RIGHT_SHOULDER), pt(lm.RIGHT_ELBOW), pt(lm.RIGHT_WRIST))
    info["Left Arm"] = "straight" if l_arm > 150 else ("highly bent" if l_arm < 60 else "bent")
    info["Right Arm"] = "straight" if r_arm > 150 else ("highly bent" if r_arm < 60 else "bent")

    l_leg = calc_angle(pt(lm.LEFT_HIP), pt(lm.LEFT_KNEE), pt(lm.LEFT_ANKLE))
    r_leg = calc_angle(pt(lm.RIGHT_HIP), pt(lm.RIGHT_KNEE), pt(lm.RIGHT_ANKLE))
    info["Left Leg"] = "straight" if l_leg > 160 else "bent"
    info["Right Leg"] = "straight" if r_leg > 160 else "bent"

    l_sh, l_hip = pt(lm.LEFT_SHOULDER), pt(lm.LEFT_HIP)
    info["Back"] = "straight posture" if abs(l_sh[0] - l_hip[0]) < 0.05 else "bent posture"

    return info


def get_font(size):
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size=size)
    except OSError:
        return ImageFont.load_default()


def draw_text_overlay(frame, info, cfg):
    pil_img = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_img)
    font = get_font(int(16 * cfg["text_size"]))
    y = 10
    for k, v in info.items():
        draw.text((10, y), f"{k}: {v}", fill=cfg["text_rgb"], font=font)
        y += int(24 * cfg["text_size"])
    return np.array(pil_img)


def draw_and_analyze(frame, results, cfg):
    if results.pose_landmarks:

        frame = draw_landmarks_pil(frame, results.pose_landmarks.landmark, cfg)

        info = analyze_pose(results.pose_landmarks.landmark)
        frame = draw_text_overlay(frame, info, cfg)
    return frame


def draw_landmarks_pil(frame, landmarks, cfg):
    pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil)
    width, height = pil.size
    for connection in mp_pose_connections.POSE_CONNECTIONS:
        start = landmarks[connection[0]]
        end = landmarks[connection[1]]
        x1, y1 = int(start.x * width), int(start.y * height)
        x2, y2 = int(end.x * width), int(end.y * height)
        draw.line([(x1, y1), (x2, y2)], fill=cfg["line_rgb"], width=cfg["line_thickness"])
    for landmark in landmarks:
        x, y = int(landmark.x * width), int(landmark.y * height)
        radius = cfg["circle_radius"]
        draw.ellipse(
            [(x - radius, y - radius), (x + radius, y + radius)],
            fill=cfg["circle_rgb"], outline=cfg["circle_rgb"],
        )
    return np.array(pil)


def process_static(frame, pose, cfg):
    pil = Image.fromarray(frame)
    pil = pil.resize((width, height), Image.Resampling.LANCZOS)
    rgb = np.array(pil)
    results = pose.process(rgb)
    return draw_and_analyze(rgb, results, cfg)


# ---------- Live camera processor ----------
class PoseProcessor(VideoProcessorBase):
    def __init__(self):
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.cfg = build_cfg()          # updated live from the main thread
        self.lock = threading.Lock()
        self.snapshot = None            # last processed frame, for download

    def recv(self, frame):
        img = frame.to_ndarray(format="rgb24")
        results = self.pose.process(img)
        with self.lock:
            cfg = self.cfg
        img = draw_and_analyze(img, results, cfg)
        with self.lock:
            self.snapshot = img.copy()
        return av.VideoFrame.from_ndarray(img, format="rgb24")


RTC_CONFIG = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

# ---------- Main ----------
st.title("Pose Detection and Analysis App")
st.write("Upload an image or video, or use your live camera to detect and analyze human poses.")

input_type = st.selectbox("Choose input type", ["Live Camera", "Upload Image", "Upload Video"])

if input_type == "Live Camera":
    st.info("Allow camera access when your browser prompts. Sliders update the stream live.")
    ctx = webrtc_streamer(
        key="pose",
        video_processor_factory=PoseProcessor,
        rtc_configuration=RTC_CONFIG,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )

    # push current slider values into the running processor every rerun
    if ctx.video_processor:
        with ctx.video_processor.lock:
            ctx.video_processor.cfg = build_cfg()

    # snapshot / download
    if ctx.video_processor and st.button("📸 Take Snapshot"):
        with ctx.video_processor.lock:
            snap = ctx.video_processor.snapshot
        if snap is not None:
            st.image(snap, channels="RGB", caption="Snapshot")
            buffer = io.BytesIO()
            Image.fromarray(snap).save(buffer, format="PNG")
            st.download_button("⬇️ Download Snapshot", buffer.getvalue(),
                               file_name="pose_snapshot.png", mime="image/png")
        else:
            st.warning("No frame captured yet — wait a moment and try again.")

elif input_type == "Upload Image":
    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file:
        image = np.array(Image.open(file).convert("RGB"))
        with mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5) as pose:
            out = process_static(image, pose, build_cfg())
        st.image(out, channels="RGB")
        buffer = io.BytesIO()
        Image.fromarray(out).save(buffer, format="PNG")
        st.download_button("⬇️ Download Result", buffer.getvalue(),
                           file_name="pose_result.png", mime="image/png")

elif input_type == "Upload Video":
    file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
    if file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())
        tfile.flush()
        tfile.close()
        try:
            container = av.open(tfile.name)
            stframe = st.empty()
            cfg = build_cfg()
            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                for packet in container.demux(video=0):
                    for frame in packet.decode():
                        img = frame.to_ndarray(format="rgb24")
                        out = process_static(img, pose, cfg)
                        stframe.image(out, channels="RGB")
            container.close()
        finally:
            os.unlink(tfile.name)

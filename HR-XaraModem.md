# 🗃️ HAMREF - 📶 Xara Modem

🗒️ Setup Reference for [Xara](https://github.com/x0rro/xara), the drop in replacement of VARA. 

**CONFIRMED WORKING** November 5, 2026 on [Linux Mint](https://linuxmint.com/).

## 📥 INSTALLATION

### Update the System

```bash
sudo apt update && sudo apt upgrade -y
```

### Install Dependencies

```bash
sudo apt install cargo-1.91 libpulse-dev libasound2-dev
```

### Install Xara Modem

⚠️ **NOTE:** use --features registered if you have a registered version of VARA. Omit otherwise.

```bash
cargo-1.91 install --locked --force --features registered --git https://github.com/x0rro/xara xara
```

## ⚙️ CONFIGURATION

```bash
cd .config && nano xara.conf
```

Copy and Paste this configuration into that file: 

```
call = ve5rev
hf = 2300
audio = alsa
capture = plughw:1,0
playback = plughw:1,0
radio
ptt = rigctld:127.0.0.1:4532
```

⚠️ **NOTE:** to determine your capture/playback device(plughw), plug in your radio via USB and run the following in terminal:

```bash
arecord -l
```

This will show you your USB device such as Card 1 ... device 0.

## 💻 OPERATION

### Start Rigctld

This is specific for the Icom 705. I have [instructions](https://jrschultz.github.io/VE5REV/posts/Winlink/#rigctld) on how to set this up for other rigs.

```bash
rigctld -m 3085 -r /dev/ttyACM0 -s 38400 -T 127.0.0.1 -t 4532 &
```

**NOTE:** You can also use FLRig instead

### Start Xara

```bash
cd ~/.cargo/bin && ./xara --config ~/.config/xara.conf
```

### Start pat winlink

```bash
pat http
```

Using pat, choose VARA HF (xara listens on the same ports). Use pat as per normal to connect to a gateway.

73 de VE5REV

# 🗃️ HAMREF - 🤖 FT-891 DIGIRIG SETTINGS

🗒️ These are the menu settings for the Yaesu FT-891 radio when using the Digirig sound card interface.

## SETTINGS:

### 1. DEEP MENU SETTINGS: Long-Press 🇫 key

| **MENU** | **SETTING** |
|-----------|------------|
| 05-06 CAT RATE | 38400bps |
| 05-07 CAT TOT | 100msec |
| 05-08 CAT RTS | DISABLE |
| 07-12 PC KEYING | OFF |
| 08-01 DATA MODE | OTHERS |                    
| 08-02 PSK TONE | 1500Hz |
| 08-03 OTHER DISP | 1500Hz | 
| 08-04 OTHER SHIFT | 1500Hz |
| 08-05 DATA LCUT FREQ | OFF | 
| 08-06 DATA LCUT SLOPE | 18dB/oct |
| 08-07 DATA HCUT FREQ | OFF | 
| 08-08 DATA HCUT SLOPE | 18dB/oct |
| 08-09 DATA IN SELECT | REAR |
| 08-10 PTT SELECT | DAKY |
| 08-11 DATA OUT LEVEL | 50 |
| 08-12 DATA BFO | USB |
| 11-07 SSB BFO | AUTO |
| 16-03 HF PWR | 30w (whatever) |
| 16-14 DATA GAIN | 50 |

### ⚠️ NOTE:

All digital modes are in USB (regardless of band). When switching back to voice mode, make sure setting 11-07 is set to **AUTO**.  

### 2. LONG-PRESS BAND > SELECT DATA MODE

### 3. SHORT-PRESS 🇫 

🔵 FUNCTION-1 MENU

🔵 Select WDH > MAX WIDTH 3000Hz 

🔵 You can long-press WDH to make it a quick button A/B/C

### 4. TURN THESE OFF: 

🔵 Noise Reduction

🔵 Processor

🔵 AGC

### ⚠️ NOTE: Recheck these settings after changing bands, they can randomly change!

🔵 Turn Down RF Gain (Until WSJTX meter is in green)

### 6. SHORT-PRESS 🇫   

🔵 SET MTR TO ALC

🔵 Adjust with WSJTX right side PWR slider

🔵 Bring ALC meter reading as low as possible (to the left)

### 7. WSJTX SETTINGS:

🔵 RADIO>RIG:FLRIG

🔵 PTT:CAT

🔵 MODE:USB

🔵 SPLIT:RIG 

--- 

### OTHER USEFUL SETTINGS

🟢 **Identify the FT-891 as a device in Linux:**

Type this into the Terminal before plugging in the USB into the computer.

```bash
sudo dmesg -w
```

Look for ```cp210x``` and which tty device it is attached to.

🟢 **Use this command for hamlib:**

This is for the hamlib rig control background daemon.

```bash
sudo rigctld -m 1036 -r /dev/ttyUSB4 -s 38400 -P RIG
```

🟠 **Alsamixer**

If you need to further tweak computer audio levels, use ```alsamixer``` in the terminal:

```bash
alsamixer
```

Press ```F6``` on the keyboard and select USB Audio Device. 

Press ```F5``` for all the audio values.

| **ITEM** | **SETTING** |
|-----------|------------|
| Speaker | 27 |
| Mic | 37 |
| Capture | 19 |
| Auto Gain Control | Muted |

### ⚠️ NOTE: These settings will change when you disconnect/reconnect the radio. So recheck as needed.

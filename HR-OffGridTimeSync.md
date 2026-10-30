# 🗃️ HAMREF - 🕙 OFF GRID MANUAL TIME SYNC

🐧 These are Linux instructions for syncing computer time without a network connection. 

💻 Time syncing is critical for digital modes.

## STEPS:

### 1. Open Terminal

### 2. Show Current Time: 

Type the following command and push <enter>.

```bash
timedatectl status
```

The Terminal will display the following:

```bash
Local time: Fri 2026-10-30 08:14:35 CST
           Universal time: Fri 2026-10-30 14:14:35 UTC
                 RTC time: Fri 2026-10-30 14:14:35
                Time zone: America/Regina (CST, -0600)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

### 3. Disable Network Time Sync (NTP)

```bash   
sudo timedatectl set-ntp 0
```

The ```sudo``` command will ask you for your password. Type it and push <enter>.

### 4. Prepare to Set Time

The time format is: yyyy-mm-dd hh:mm:ss format; hh is 0-23.
Get this from your off grid time source (a GPS or a radio like the ICOM 705). 

Type the following:

```bash  
sudo timedatectl set-time “2026-10-30 08:15:00”
```

Set the seconds a bit ahead so you can manually line up the time sync. 

When the seconds line up:

### 5. Press <enter> on the keyboard.

### 🛰️ Your computer time is now in sync with the GPS time!

---

### 6. On Grid Syncing

When you want to go back to network time sync:

```bash
sudo timedatectl set-ntp true
```

### 7. Force a Time-Sync Refresh

This is a useful command if your digital mode time is wonky for any reason whilst on grid:

```bash
sudo systemctl restart systemd-timesyncd.service
```

73 de VE5REV
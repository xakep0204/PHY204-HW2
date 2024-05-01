import subprocess
import threading

times = []

def run_solver_grapher(L=10):
    cmd_solver = f"python3.10 solver.py {L}"
    cmd_grapher = f"python3.10 grapher.py {L}"
    t_solver = float(subprocess.check_output(cmd_solver, shell=True).decode("utf-8").strip())
    t_grapher = float(subprocess.check_output(cmd_grapher, shell=True).decode("utf-8").strip())
    print(f"L={L} t_solver={t_solver} t_grapher={t_grapher}")
    times.append((L, t_solver, t_grapher))

ths = []
for i in range(10, 110, 10):
	ths.append(threading.Thread(target=run_solver_grapher, args=(i,)))
     
for th in ths:
  th.start()
  
for th in ths:
  th.join()
     

print("| L   | solver.py  | grapher.py |\n| --- | ---------- | ---------- |")
for data in times:
  print(f"| {data[0]:>3} | {data[1]:>10.3f} | {data[2]:>10.3f} |")
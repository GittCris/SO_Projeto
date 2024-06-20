import subprocess

def evaluefunction(outfile,scheduler='FIFO', jobs=3, seed=100, job_list=[], quantum=1):
    cmd_list = ['python3', 'scheduler.py', '-p', scheduler, '-j', str(jobs), '-s', str(seed), '-l', ','.join(map(str, job_list)), '-c']
    if scheduler == 'RR':
        cmd_list.extend(['-q', str(quantum)])
    subprocess.run(cmd_list,stdout=outfile, stderr=subprocess.STDOUT)

def run_mlfq(params, outfile):
    cmd = ['python3', 'mlfq.py'] + params
    subprocess.run(cmd, stdout=outfile, stderr=subprocess.STDOUT)

def cap7():
    for case_num in range(1, 7):
        print(f'EX {case_num} Concluído')
        with open(f"output_cap7_{case_num}.txt", "a") as outfile:
            match case_num:
                case 1:
                    list_jobs = [200, 200, 200]
                    evaluefunction(outfile,'FIFO', 3, 0, list_jobs)
                    evaluefunction(outfile,'SJF', 3, 0, list_jobs)
                case 2:
                    list_jobs = [100, 200, 300]
                    evaluefunction(outfile,'FIFO', 3, 0, list_jobs)
                    evaluefunction(outfile,'SJF', 3, 0, list_jobs)
                case 3:
                    list_jobs = [200, 200, 200]
                    evaluefunction(outfile,'RR', 3, 0, list_jobs)
                    list_jobs = [100, 200, 300]
                    evaluefunction(outfile,'RR', 3, 0, list_jobs)
                # esse caso mostra que trabalhos de diferentes durações
                # tem ordens de execução diferentes
                case 4:
                    list_jobs = [300, 200, 100]
                    evaluefunction(outfile,'FIFO', 3, 0, list_jobs)
                    evaluefunction(outfile,'SJF', 3, 0, list_jobs)
                case 5:
                    list_jobs = [200, 200, 200]
                    evaluefunction(outfile,'SJF', 3, 0, list_jobs)
                    evaluefunction(outfile,'RR', 3, 0, list_jobs,quantum=200)

                case 6:
                    list_jobs = [1, 1, 1]
                    evaluefunction(outfile,'SJF', 3, 0, list_jobs)
                    list_jobs = [100, 100, 100]
                    evaluefunction(outfile,'SJF', 3, 0, list_jobs)
                    list_jobs = [1000, 1000, 1000]
                    evaluefunction(outfile,'SJF', 3, 0, list_jobs)





def cap8():
    for case_num in range(1, 7):
        print(f'EX {case_num} Concluído')
        with open(f"output_cap8_{case_num}.txt", "a") as outfile:
            match case_num:
                case 1:
                    #dois trabalhos -n 2; duas filas -j 2;limitando tamanho -m 2; desativando I/O -M 0
                    #Simulando o comportamento de um escalonador mlfq
                    #De T = 0 a T = 10 a tarefa0 executa com prioridade 1
                    #De T = 10 a T = 20 a tarefa0 executa com prioridade 0
                    #De T = 20 a T = 30, a tarefa 1 chega com prioridade 1
                    #De T = 30 a T = 40 a tarefa 0 executa até o fim com prioridade 0
                    # A partir de T = 40 a tarefa 1 executa até o fim
                    run_mlfq(['-n', '2','-j','2', '-m', '2','-M','0', '-l', '0,30,0:20,20,0', '-c'], outfile)
                case 2:
                    #EX1
                    #-n =3, l = 0:200:0
                    run_mlfq(['-n','3','-l','0,200,0','-c' ],outfile)
                    #EX2
                    #Tarefa B chega no T 100 e dura por 20ms
                    run_mlfq(['-n','3','-l','0,180,0:100,20,0','-c'],outfile)
                    #EX3
                    #-S para manter a propriedade da regra 4b da tarefa b
                    #Tarefa B sendo executada desde T = 50ms, 25x, com I/0 de 1ms
                    #-i I/O a cada 5ms
                    run_mlfq(['-S','-n','3','-l','0,175,0:50,25,1','-i','5','-c' ],outfile)
                case 3:
                    # Definindo o número de filas no MLFQ como 1. 
                    # Isso cria uma fila única, eliminando o comportamento multinível do MLFQ e 
                    # simulando o round-robin, onde todos os processos são tratados igualmente.
                    run_mlfq(['-n','1', '-q','5','-l','0,10,0:0,10,0','-c' ],outfile)
                case 4:
                   run_mlfq(['-S','-I', '-n', '2','-q','100', '-l', '0,198,99:0,2,0','-i','1', '-c'],outfile)
                case 5:
                    #-B: 200ms
                    run_mlfq(['-n', '2', '-B', '200','-l', '0,200,0:0,200,0','-i','1', '-c'], outfile)
                case 6:
                    #Com e sem -I
                    run_mlfq(['-i','1', '-n', '2','-l', '0,20,5:0,20,5', '-c'], outfile)
                    run_mlfq(['-I','-i','1', '-n', '2','-l', '0,20,5:0,20,5', '-c'], outfile)



def main():
    cap7()
    cap8()

if __name__ == '__main__':
    main()
    

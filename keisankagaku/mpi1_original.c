#include <stdio.h>
#include <mpi.h>

#define N 10

int main(int argc, char **argv){
  int my_rank, num_proc;
  int i, arr[N];

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &num_proc);
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  if (my_rank == 0){
    for (i = 0; i < N; i++){
      arr[i] = i * i;
    }
    MPI_Send(???);
  }

  if (my_rank == 1){
    MPI_Recv(???);
    for (i = 0; i < N; i++){
      printf("%d\n",arr[i]);
    }
  }

  MPI_Finalize();

  return 0;
}
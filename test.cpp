typedef struct MemRef_descriptor_ *MemRef_descriptor;
typedef struct MemRef_descriptor_ {
  float *a;
  float *b;
  long c;
  long d[4];
  long e[4];
} Memref;
int main(int argc, char **argv){
    int dev_id= atoi(argv[1]);
    int num_threads = 1;
    hthread_dev_open(dev_id);
    hthread_dat_load(dev_id, "kernel.dat");
    MemRef_descriptor input = hthread_malloc(dev_id, sizeof(Memref), HT_MEM_RW);
    MemRef_descriptor output = hthread_malloc(dev_id, sizeof(Memref), HT_MEM_RW);
    int size = 3 * 224 * 224;
    int outsize = 1000;
    float *a1 = hthread_malloc(dev_id, size * sizeof(float), HT_MEM_RW);
    float *b1 = hthread_malloc(dev_id, size * sizeof(float), HT_MEM_RW);
    for(int i=0;i<150528;i++){
        a1[i] = 1;
        b1[i] = 1;
    }
    input -> a = a1;
    input -> b = b1;
    input -> c = 0;
    input -> d[0] = 1;
    input -> d[1] = 3;
    input -> d[2] = 224;
    input -> d[3] = 224;
    input -> e[0] = 150528;
    input -> e[1] = 50176;
    input -> e[2] = 224;
    input -> e[3] = 1;
    float *a2 = hthread_malloc(dev_id, size * sizeof(float), HT_MEM_RW);
    float *b2 = hthread_malloc(dev_id, outsize * sizeof(float), HT_MEM_RW);
    for(int i=0;i<outsize;i++){
        b2[i] = 0;
    }
    output -> a = a2;
    output -> b = b2;
    unsigned long args[2];
    args[0] = (unsigned long)output;
    args[1] = (unsigned long)input;
    double t_start, t_end;
    int tg_id = hthread_group_create(dev_id, num_threads);
    hthread_group_wait(tg_id);
    int error_num = 0;
    for(int i=0; i<NUM_TESTS; i++){
        hthread_group_exec(tg_id, "_mlir_ciface_forward", 0, 2, args);
        hthread_group_wait(tg_id);
    }
    printf("[output]:\n[[");
    for(int i=0;i<outsize;i++){
        printf("%e,", output -> b[i]);
    }
    printf("]]\n");
    printf("[run time]: %lf(s)\n", (t_end - t_start) / 1e6);
    hthread_group_destroy(tg_id);
    hthread_free(a1);
    hthread_free(b1);
    hthread_free(a2);
    hthread_free(b2);
    hthread_dev_close(dev_id);
    return 0;
}
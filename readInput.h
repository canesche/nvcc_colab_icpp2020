#ifndef __READINPUT_H
#define __READINPUT_H

void readInput() {

    if (fptr == NULL) {
        printf("Error! opening file");
        exit(1);
    }

    int c = 0, n1, n2;
    while(fscanf(fptr, "%d %d", &n1, &n2) != EOF) {
      if (c == 0) {
		      nodes = n1;
          edges = n2;
          e_a = new uint8_t[edges];
          e_b = new uint8_t[edges];
      } else {
          e_a[c-1] = n1;
          e_b[c-1] = n2;
      }
      c++;
    }

    fclose(fptr);
}

#endif
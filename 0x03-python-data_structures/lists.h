#ifndef LIST_H
#define LIST_H
#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
    int val;
    struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head);

#endif

#include "lists.h"

/**
 * insert_node - function that
 * Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *my_node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (my_node == NULL || my_node->n >= number)
	{
		new->next = my_node;
		*head = new;
		return (new);
	}

	while (my_node && my_node->next && my_node->next->n < number)
		my_node = my_node->next;

	new->next = my_node->next;
	my_node->next = new;

	return (new);
}

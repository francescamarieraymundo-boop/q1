# ctskillsArayatLN

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/francescamarieraymundo-boop/q1)

# Step 1. Annex A
## Main problem

The PSHS school canteen crowds during break times and lunch periods. The vendors lack a system, hence manual labor is done, causing inefficiency

## Step 2. Sub problems

1. No system for food stock - Food stock is not tracked correctly, so it would take time to manually view the inventory and see what to order in bulk. This would take days before an, essentially popul[...]
2. Long queues - Students are affected by the long waiting times. In unlucky situations, they end up not eating at all when the queue takes too long and fills the entire period before they could e[...]
3.  No program for calculation - Manual calculation of totals and change. This contributes to the time problem, and risks miscalculation alongside inefficient methods as they lack a program to mak[...]
4. Slow payment methods - As everything is manual, the student would take too long to order given the lack of a clear structure of ordering. Alongside this, labels aren't clear so it may affect th[...]

   
## Step 3. Table
| Sub-problem | CT-Skill | Example Soluition |
| :--- | :---: | ---: |
| No system for food stock | Pattern recognition | Moniter patterns and trends of sales and popular, high in demand items |
| Long queues | Decomposition | Identify the core reasons, lack of sufficient payment methods and factoring in student's personal decisiveness and environmental factors |
|  No program for calculation | Generalization/Algorithmic Thinking | - Generalization: Making a general program for payment and ordering in general, involving digital payment methods alongside di[...]
|  Slow payment methods and ordering time | Algorithmic thinking | Structured steps for ordering and a clear, adaptable system |

## Step 4. Pseudocode

```bash
1. No system of tracking food stock

START
FOR each day:
Record the quantity sold for every food item
Record the quantity of each item remaining

FOR each food item:
Compare sales across different days 
Identify items with consistently high sales
Identify items with consistently low sales

IF an item has high and consistent demand:
Increase its expected stock the following day

IF an item has low and consistent demand:
Decrease/retain the current stock the following day 

Repeat the process daily

END

2. Long queues

START

Identify possible causes of long queues:
Check the number of available payment methods
Check the time students spend deciding what to order
Check if food labels and prices are clear
Check if ordering area is organized
Check if food space is sufficient

FOR each identified cause:
Determine how much it contributes to the queue

IF there are insufficient payment methods:
Add or improve available payment methods

IF students take too long to decide:
Provide clear food labels, prices and menus

IF the ordering area is poorly organized:
Improve the arrangement and flow of the area

IF the food space causes delays:
Rearrange the space for easier movement

Repeat the observation and improvement process

END

3. No program for calculation (I couldn't decide between generalization and AT, but the program for AT makes more sense,, here's both though)

- Generalization:

START

Identify steps:
Select food items
Identify item prices
Enter quantities
Calculate the total cost
Enter payment
Calculate change
Display the result

the system would work for:
Different food items
Different quantities
Different payment methods
Different order totals

END

- Algorithmic thinking:

START

Display the list of food items and prices

INPUT selected food item
INPUT quantity

calculate:
Item total = price x quantity

Repeat for every selected item

Calculate:
Total cost = sum of all item totals

INPUT payment method

IF payment method is digital:
Process digital payment

ELSE:
INPUT amount paid
Calculate:
Change = amount paid - total cost
Display change

Display:
Order summary
Total cost
Payment status

END
```

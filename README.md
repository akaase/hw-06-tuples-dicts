# Assignment: Python Data Structures - Tuples, Sets, and Dictionaries

In this homework, you're going to write code for two challenge problems.

You'll practice these programming concepts we've covered in class:

* Using dictionaries to solve problems.
* Storing data in tuples and sets.

## Deliverables

1. **Fork** the assignment repo
1. **Clone** your fork of the assignment repo
1. **Commit** your solution
1. **Push** to Github when you are done

## Submitting

To submit this assignment:

1. Go to the [assignment's main repo](https://git.generalassemb.ly/PYTHR-august-2019/hw-08-tuples-and-dictionaries)
1. Click the **Issues** tab
1. Click the **New Issue** button
1. In the Title field, fill in your name
1. In the comment field, paste the URL to your assignment repo
1. Click **Submit new issue** and you're done!

---

# Part 1: I Love You, Tuple

Create a file called `part1.py` and write your solution code in there.

You may recall tuples from your in-class lesson. Tuples are *immutable* data structures, which means they can't be changed after they're created.

They are typically used to store related information that doesn't need to be changed, such as a student record or, in this case, some stats about a movie.

It's your job to create some `print` statements that access the appropriate values inside each tuple to produce the expected output.

### Starter Code

```python
# My favorite romance movies
# title, release year, runtime, tagline, main characters
romantic_movie1 = ('The Princess Bride', 1987, 98, 'The story of a man and a woman who lived happily ever after.', ['Buttercup', 'Westley', 'Fezzik', 'Inigo Montoya', 'Vizzini'])
romantic_movie2 = ('Groundhog Day', 1993, 101, "He's having the day of his life… over and over again.", ['Phil Connors'])
romantic_movie3 = ('Amélie', 2001, 122, 'One person can change your life forever.', ['Amélie Poulain', 'Nino Quincampoix', 'The Garden Gnome'])
```

### Expected Output

```
Here are my favorite romance movies:

The Princess Bride ( 1987 ): The story of a man and a woman who lived happily ever after.

Groundhog Day ( 1993 ): He's having the day of his life...over and over again.

Amélie ( 2001 ): One person can change your life forever.
```

**Hint:** Remember, you can access a tuple sort of like a list, with the square brackets `[]` counting from zero (e.g., the value of `romantic_movie1[0]` is `"The Princess Bride"`).

### Bonus:

Look up how to change the `print` statement's separator character to an empty string `''` instead of a space so that you can print the year as `(1987)` instead of `( 1987 )`. You'll have to do some independent research to figure this out.

---

# Part 2: Friends, Colleagues, and Details

Create a file called `part2.py` and write your solution code in there.

Your boss tasks you with creating a company directory.

Make a list called `employees`, which will contain one dictionary per person and include the keys `name`, `age`, `department`, `phone`, and `salary`.

Once you have the list of dictionaries set up, loop through the list and print out the `name`, `department`, and `phone` number of each employee. Their `age` and `salary` should remain secret!

### Starter Code

A dictionary should be set up in the following way:

```python
{
    'name': 'Jill Swanson',
    'age': 55,
    'department': 'Management',
    'phone': '555-1234',
    'salary': '$87,000'
}
```

### Expected Output

```
Jill Swanson in Management can be reached at 555-1234.
Leslie Knope in Middle Management can be reached at 555-4321.
Andy Dwyer in Shoe Shining can be reached at 555-1122.
April Ludgate in Administration can be reached at 555-3345.
```

**Hint:** Dictionaries have values that can be accessed with keys, for example, `employees['name']`. Keys are typically strings but can be numbers also.

# Part 3: Reverse Lookup

_Part 3 is **optional**. You are **not expected** to complete this part, but you could probably use the practice, so please do it!_

Create a file called `part3.py` and write your solution code in there.

Finding the value from a key is easy: `my_dictionary[key]`. But, what if you only have the value and want to find the key?

You task is to write a function, `reverse_lookup()`, that takes a dictionary and a value and returns the corresponding key.

For example:

```python
state_capitals = {
    'Alaska' : 'Juneau',
    'Colorado' : 'Denver',
    'Oregon' : 'Salem',
    'Texas' : 'Austin'
}

print(reverse_lookup('Denver'))
#--> Colorado
```

---

# Celebrate!

You're all finished!

![](https://media.giphy.com/media/UkhHIZ37IDRGo/giphy.gif)

# Object-Oriented Programming
* Exercise [Links](https://github.com/ekeleshian/data_structures_and_algorithms/blob/master/object_oriented_programming.py) By: [Elizabeth Keleshian](https://ekeleshian.github.io/)



___

## <u> Goals, Principles, and Patterns. </u>

___

### <u> Object-Oriented Design Goals. </u>

#### 1. Robustness:

- A program produces the right output for all the anticipated inputs in the program’s application.
- Capable of handling unexpected inputs that are not explicitly defined for its application.

#### 2. Adaptability:

- Software is that it achieves adaptability (also called `evolvability`).

#### 3. Reusability:

- Same code should be usable as a component of different systems in various
  applications.

### <u> Object-Oriented Design Principles. </u>

#### 1. Modularity

- Modularity refers to an <ins> organizing principle </ins> in which different components
  of a software system are divided into separate functional units.
- Modularity in a software system can also provide a powerful organizing framework that brings clarity to
  an implementation.
- For example,
    * math module, which provides definitions for key
      mathematical constants and functions,
    * os module, which provides support
      for interacting with the operating system.
- Importance:
    * Testing & debugging
    * Tracing bugs
    * Reusability
    * Robustness

> ***Provide a powerful organizing framework that brings clarity to an implementation.*** <br/>
> ***This is particularly relevant in a study of data structures, which can typically be designed with sufficient
abstraction and generality to be reused in many applications***.

#### 2. Abstraction

- Abstraction is to distill a complicated system down to its most fundamental parts.
- Typically, describing the parts of a system involves naming them and
  explaining their functionality.

*
    * <i>Applying the abstraction paradigm to the design of
      data structures gives rise to abstract data types (ADTs). An ADT is a mathematical
      model of a data structure that specifies the type of data stored, the operations supported on them, and the types of parameters of the operations.  </i>
    * <i> Python supports abstract data types using a mechanism known as an abstract base class (ABC).</i>

#### 3. Encapsulation

- Different components of a software system should not reveal the internal details of their
  respective implementations..

### <u>Design Patterns. </u>

- Design patterns in this context shows how they(design patterns) can be
  consistently applied to implementations of data structures and algorithms.
- A pattern provides a general template for a solution that can be applied in
  many situations.

*
    * Pattern consist of:
    * a name - which identifies the pattern;
    * a context - which describes the scenarios for which this pattern can be applied;
    * a template - which describes how the pattern is applied;
    * a result - which describes and analyzes what the pattern produces.
*
    * Design patterns main groups are:
    * patterns for solving  <b>ALGORITHM DESIGN</b> problems
    * patterns for solving <b>SOFTWARE ENGINEERING</b> problems.

##### ALGORITHM DESIGN PATTERNS.

*
    * Recursion
    * Amortization
    * Divide-and-conquer
    * Prune-and-search, also known as decrease-and-conquer
    * Brute force
    * Dynamic programming
    * The greedy method

##### SOFTWARE ENGINEERING PATTERNS.

*
    * Iterator
    * Adapter
    * Position
    * Composition
    * Template method
    * Locator
    * Factory method

## <u> Software Development. </u>

Three major steps are:

1. Design
2. Implementation
3. Testing and Debugging

___

### Design

- Design step we decide

*
    * how to divide the workings of our program into classes.
    * how these classes will:
        * interact,
        * what data each will store,
        * what actions each will perform.

- Rules of thumb to apply when determining how to design classes:

*
    * Responsibilities - Divide the work into different actors, each with a different responsibility.
    * Independence - Define the work for each class to be independent of other classes as possible.
    * Behaviors - Define the behaviors for each class carefully and precisely, so
      that the consequences of each action performed by a class will be well understood by other classes that interact with it

> ***Defining the classes, together with their instance variables and methods, are key
to the design of an object-oriented program.***

#### How to deign: Software Development.

- High level design uses class-Responsibility-Collaborator (CRC) cards.
- CRC cards are index cards that subdivide the work required of a program.
- Each card represent a component, which will ultimately become a class in the program.
    * Write the name of each component on the top of an index card.
    * On the left-hand side, write the responsibilities for this component.
    * On the right-hand side, list the collaborators for this component.
        * that is, other components that this component will have to interact with to perform its duties.
    * Example.

| Class name     |              |
|----------------|--------------|
| Responsibility | Collaborator |

| Room                                                                               |          |
|------------------------------------------------------------------------------------|:--------:|
| Building<br/>Room No.<br/> Type(..lab, class)<br/> No. seats<br/>Get Building Name | Building |

| Building                                                         |      |
|------------------------------------------------------------------|:----:|
| Building Name<br/>Rooms <br/> Provide Name<br/>Provide Available | Room |

*
    * The design is complete when all actions have been assigned to actors(classes).
    * Documenting design use UML unified modeling language

| Class Name: CreditCard                                                                           |
|:-------------------------------------------------------------------------------------------------|
| Fields: <i> &nbsp;&nbsp;&nbsp;&nbsp; </i>  `_customer _bank _account _balance _limit`            |        
| Behaviors: <i> &nbsp;&nbsp;&nbsp; </i>  `get_Customer() get_Bank() get_Balance() make_payment()` |


### Pseudo-Code
- Is intermediate step before the implementation of a design that describes algorithms in a way 
that is intended for human eyes only.
### Testing and Debugging
- Process of experimentally checking the correctness of a program AND process of tracking the execution of a 
program and discovering the errors in it.
#### Testing
- Programs often tend to fail on special cases of the input.
- It is  advantageous to run the program on a large collection of randomly generated inputs.
- Top-down testing proceeds from the top to the bottom of the program hierarchy.
- For example; 
  * if function A calls
  function `B` to get the first line of a file, when testing `A` we can replace B with a stub
  that returns a fixed string.
- Bottom-up testing proceeds from lower-level components to higher-level components.
- For example;
  * Bottom-level functions, which do not invoke other functions,
  are tested first, followed by functions that call only bottom-level functions, and so
  on. Similarly, a class that does not depend upon any other classes can be tested
  before another class that depends on the former. This form of testing is usually
  described as unit testing, as the functionality of a specific component is tested in
  isolation of the larger software project.

## <u> Class Definitions. </u>

View `objects.py`
___
### Operator Overloading and Python’s Special Methods
* * Python’s built-in classes provide natural semantics for many operators. <br/>
  * Syntax `a+b` invokes addition for numeric types, and concatenation for
sequence types.
* * These built-in classes provide what to perform when overloading certain operators.
  * Evaluating the expression, `a+b`, for instances of a user-defined `class`
without `__add__` or `__radd__` will raise an error.

## <u> Class Inheritance. </u>

View `objects.py`
___

## <u> Abstract Base Classes. </u>
___
 * * An abstract base class if its only purpose is to serve as a base class through inheritance.
   * An abstract base class is one that cannot be directly instantiated, 
   * A concrete class is one that can be instantiated. 
   * > By these definition, `Class Progression`is
   technically concrete, although we essentially designed it as an abstract base class.

* * The template method pattern is
when an abstract base class provides concrete behaviors that rely upon calls to
other abstract behaviors. 
  * In that way, as soon as a subclass provides definitions for
  the missing abstract behaviors, the inherited concrete behaviors are well-defined.




















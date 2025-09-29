# cs117-lab3
1. Assembly Reflections

Q. What did you notice about registers and instructions?

In Assembly, I noticed that registers are like tiny storage spots in the CPU where data is held temporarily. You have to tell the computer exactly which register to use and what to do with it. The instructions are very simple and specific, like "move this number here" or "add these two values." Everything has to be done step-by-step with no shortcuts.

Q. How is coding in Assembly different from Python?

Assembly is much more detailed. You have to control almost everything yourself, like where data is stored and how it's used. In Python, you can just write simple lines like x = 5 and it works. In Assembly, you'd need multiple lines just to do that. Python hides a lot of the hard work, but Assembly shows you how the computer really works behind the scenes.

2. Python Reflections

Q. Why is Python easier/faster for building the same project?

Python is easier because it lets you write less code to do more things. It takes care of the little details for you, so you can focus on the big picture. It’s also faster to write and understand, especially for beginners.

Q. Which features of Python help abstraction (variables, functions, loops)?

Variables let you store data with simple names, like score = 10, so you don’t need to worry about memory or registers.
Functions let you group code together and reuse it. You can write it once and use it many times, which saves time.
Loops let you repeat actions easily without writing the same line over and over again.
These features help you think more about what you want to do, and less about how the computer does it.

3. Comparison Table

| Feature | Assembly Example | Python Example | Notes |
| :--- | :--- | :--- | :--- |
| *Variable storage* | Register (EAX) | x = 5 | In Assembly, you store values directly in hardware parts like registers. In Python, you just use easy-to-read variable names to hold data. |
| *Printing output* | INT 21h | print() | Assembly needs a special command (like a system call) to talk to the computer for things like printing. In Python, you just use a simple function that handles all the hard work for you. |
| *Arithmetic* | ADD AX, BX | x + y | Assembly uses short codes (called mnemonics) to do math with registers. Python lets you use normal math symbols with variables, which is easier to read and write. |

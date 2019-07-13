#             《代码的整洁之道》读书笔记

## 第一章 整洁代码：回答了一个核心问题什么是整洁的代码

### 不同的人有不同的看法：

**Bjarne：**

1. 整洁的代码逻辑直接了当，使得缺陷容易暴露；
2. 尽量减少依赖关系，便于维护；
3. 依据某种分层战略完善错误处理的代码（疑问：何种分层战略？）；
4. 性能调至最优，尽可能的减少运算周期（对算法能力有一定的要求）。

**Grandy：**

1. 干净利落的抽象。理解为所抽象出来的对象只包含自己必需的东西。

**Ron：**

1. 能通过所有测试；
2. 没有重复的代码；
3. 体现系统中的全部设计理念；
4. 包括尽量少的实体，比如类、方法、函数等。

### 总结

1. 整洁的代码要具有完整的功能性，不会因代码的简洁而无法完成它要做的事情；

2. 阅读代码在编写代码的过程中占很大的一部分。为函数、变量等元素起一个有意义的名字更加便于阅读；

3. 减少代码之间的耦合性，更改一部分代码时不会影响到其他代码的使用，这样便于更好的维护代码；

4. 善用抽象，重复的代码块，抽象成一个可复用的方法或者类；

5. 针对任何的一个容器，我们都需要实现从这个容器集合中找到某一个特定的条目。将该需求的实现封装到一个抽象的方法或者类中可以更加有效地处理代码，同时也为未来的修改留下余地。




## 第二章 有意义的命名：需要注意哪些命名？命名的规则有哪些？

### 需要注意哪些命名：

变量名、函数名、参数名、类名、封包名、代码文件名、工程目录名、资源文件名等一切在代码过程中需要自己起名字的东西。

### 命名规则有哪些：

#### 规则一：名副其实

简单来说就是对象的名称要符合其实际用途的需要。



```c#
eg:
public List<int[]> getThem(){
    List<int[]> list1 = new ArrayList<int[]>();
    for(int[] x : theList)
        if(x[0] == 4)
            list1.add(x);
    return list1;
}
```

代码的整洁不在于代码是否简洁，而在于代码的模糊度：即上下文在代码中未被明确体现的程度。上述代码所表达的内容回事我们产生如下疑问：

1. `theList` 是什么？
2. `theList[0]`代表什么？
3. 值4代表什么？
4. 需要如何使用返回的列表？

以扫雷游戏为例，`theList`代表的是整个棋盘的单元格列表，我们可以将其命名为`gameBoard`。`gameBoard`上每一个单元格用一个数组表示（标明行和列以及标记状态），其中零下标表示的是状态值，值为4时，表示该单元格以被标记。此时，我们可以将代码改为：

```C#
public List<int[]> getFlaggedCells(){
    List<int[]> flaggedCells = new ArrayList<int[]>();
    for(int[]cell: gameBoard)
        if(cell[STATUS_VALUE] == FLAGGED)
            flaggedCells.add(cell);
    return flaggedCells;
}
```

这么一来我们就知道该函数使用来获取所有被标记过的单元格了。更进一步地，我们可以用一个类来表示单元格，创建一个`IsFlagged`的函数，从而掩盖掉4这个魔术数。此时代码可以改进为：

```c#
public List<Cell> GetFlaggedCells(){
    List<Cell> flaggedCells = new ArrayList<Cell>();
    for(Cell cell : gameBord)
        if(cell.IsFlagged())
            flaggedCells.add(cell);
    return flaggedCells;
}
```

#### 规则二：避免误导

1. 尽量避免在开发平台上会出现的专有名词。
2. 在编写集合类型的对象名称时，要注意尽量避免在名称中出现容器类型。例如accountList表示一组账号，即使所使用的容器真的是List也尽量不要使用List做结尾，可以改用accounts、accountGroup等。
3. 在编写代码时尽量不要让“l"和“O"出现在变量的开头或者结尾或者单独作为变量，因为其在某些字体下有可能会与”1“和”0“混淆。

#### 规则三：做有意义的区分

先举一个例子：

```c#
public static void copyChars(char a1[], char a2[]){
    for(int i = 0; i < a1.length; i++){
        a2[i] = a1[i];
    }
}
```

参数两个都是字符数组类型，`a1`，`a2`虽然满足编译器不重名的需求，但是可读性很差。将其改为`source`和`destination`，会使代码清晰许多。

代码中不要出现无意义的冗余。例如`Product` 和`ProductInfo`几乎没有区别，尽量不要使用这种添加后并不会带来实质区别的改变。

代码中不要出现对象的类型名。Variable一词不要出现在变量中，Table不要出现在表名中，Name很显然是字符串，就没有必要在写成`NameString`了。

综上所述，不同对象之间的命名要以读者能够界别其不同之处的方式来区分。

#### 规则四：使用读得出来的名称

不要使用自造词，会降低代码可读性，使用恰当的英文单词（实在不行中国人用拼音也行）来编写代码。

#### 规则五：使用可搜索的名称

数字常量和单字母名称在大片的工程代码中是很难找出来的。为数字赋予一个变量名，或者将其编写成一个const 常量。这样会使得对象更加容易搜索。

**单字母名称仅用于短方法中的本地变量。名称的长短应与其作用域的大小相对应。若变量或常量在代码的多处使用，则应赋予其以便于搜索的名称。**

以下代码段作比较：

```c#
for(int j = 0; j < 34; j++){
    s += (t[j] * 4) / 5;
}
和
int realDaysPerIdealDay = 4;
const int WORK_DAYS_PER_WEEK = 5;
const int NUMBER_OF_TASKS = 34;
int sum = 0;
for(int j = 0; j < NUMBER_OF_TASKS; j++){
    int realTaskDays = taskEstimate[j] * realDaysPerIdealDay;
    int realTaskWeeks = (realdays / WORK_DAYS_PER_WEEK);
    sum += realTaskWeeks;
}
```

#### 规则六：避免使用编码

不要对对象的名称进行编码（人工编码，类似于命名的协议）。尽量不要使用成员前缀、接口端也不尽量不要加修饰。

#### 规则七：避免思维映射

**明确才是王道。**不要编写别人不能理解的代码。

#### 规则八：类名多用名词、方法名多用动词

#### 规则九：每个概念对应一个词

举例说明：fetch、retrieve、get都表达拿的意思，统一使用一个单词做为拿的概念。

#### 规则十：不要使用双关语

举例说明：add既可以表示在末尾加入、也可以表示插入，应该使用append和insert进行区分。

#### 规则十一：添加有意义的语境

对于一些供外部使用的对象，添加相关联的语境前缀使对象的使用环境更加明确。对比如下代码：

```c#
private void PrintGuessStatistics(char candidate, int count){
    String number;
    String verb;
    String pluralModifier;
    if(count == 0){
        number = "no";
        verb = "are";
        pluralModifier = "s";
    }else if(count == 1){
        number = "1";
        verb = "is";
        pluralModifier = "";
    }else{
        number = Integer.toString(count);
        verb = "are";
        pluralModifier = "s";
    }
    String guessMessage = String.format("There %s %s %s%s", verb, number, candidate, pluralModifier);
    print(guessMessage);
}

```

创建一个`GuessStatisticsMessage`的类，把方法中的number、verb、pluralModifier变量变成该类的成员字段。在使用时增加了语境使得代码更加干净利落。

```c#
//可以看得出函数都是靠Alt + Enter自动生成的。
public class classGuessStatisticsMessage{
    private String number;
    private String verb;
    private String PluralModifier;
    public String make(char candidate, int count){
    CreatePluralDependtMessageParts(count);
    return Stirng.format("There %s %s %s%s", verb, number, candidate, pluralModifier);
    }
    private void CreatePluralDependtMessageParts(int count){
        if(count == 0)
            ThereAreNoletters();
        else if(count == 1)
            ThereIsOneletter();
        else
            ThereAreManyLetter(count);
    }
    private void ThereAreManyLetter(int count){
        number = Integer.toString(count);
        verb = "are";
        pluralModifier = "s";
    }
    private void ThereIsOneletter(){
        number = "1";
        verb = "is";
        pluralModifier = "";
    }
    private void ThereIsOneletter(){
        number = "no";
        verb = "are";
        pluralModifier = "s";
    }
}

```



## 第三章函数


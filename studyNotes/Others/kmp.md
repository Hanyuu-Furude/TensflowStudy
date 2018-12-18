# 简单字符串匹配算法
## 1. 暴力匹配法
定义现有文本串S模式串P，假设现在文本串S匹配到i位置，模式串P匹配到j位置，则有：
* 如果当前字符匹配成功（即S[i] == P[j]），则i++，j++，继续匹配下一个字符；
*如果失配（即S[i]! = P[j]），令i = i - (j - 1)，j = 0。相当于每次匹配失败时，i 回溯，j 被置为0。
``` cpp
int ViolentMatch(char* s, char* p)
{
	int sLen = strlen(s);
	int pLen = strlen(p);
 
	int i = 0;
	int j = 0;
	while (i < sLen && j < pLen)
	{
		if (s[i] == p[j])
		{
			//当前字符匹配成功（即S[i] == P[j]），则i++，j++    
			i++;
			j++;
		}
		else
		{
			//失配（即S[i]! = P[j]），令i = i - (j - 1)，j = 0    
			i = i - j + 1;
			j = 0;
		}
	}
	//匹配成功，返回模式串p在文本串s中的位置，否则返回-1
	if (j == pLen)
		return i - j;
	else
		return -1;
}
```
>		暴力匹配法没有利用已经匹配过的信息，实现简单但是效率低下。
***
## 2.KMP算法
> Knuth-Morris-Pratt 字符串查找算法，简称为 “KMP算法”，常用于在一个文本串S内查找一个模式串P 的出现位置，这个算法由Donald Knuth、Vaughan Pratt、James H. Morris三人于1977年联合发表，故取这3人的姓氏命名此算法。
* 算法流程
  * 假设现在文本串S匹配到i位置，模式串P匹配到j位置 
    * 如果j=-1，或者当前字符匹配成功（S[i]==P[j]），都令i++，j++，继续匹配下一个字符；
    * 如果j!=-1，且当前字符匹配失败（S[i]!=P[j]），则令i不变，j =next[j]。此举意味着失配时，模式串P相对于文本串S向右移动了j-next[j] 位。\
  	（当匹配失败时，模式串向右移动的位数为：失配字符所在位置 - 失配字符对应的next 值（next 数组的求解会在下文阐述），即移动的实际位数为j-next[j]，且此值大于等于1。next数组的值代表当前字符之前的字符串中，有多大长度的相同前缀后缀。例如如果next[j]=k，代表j之前的字符串中有最大长度为k 的相同前缀后缀。此也意味着在某个字符失配时，该字符对应的next值会告诉你下一步匹配中，模式串应该跳到哪个位置（跳到next[j]的位置）。如果next[j]等于0或-1，则跳到模式串的开头字符，若next[j]=k且k>0，代表下次匹配跳到j之前的某个字符，而不是跳到开头，且具体跳过了k个字符。)
``` cpp
int KmpSearch(char* s, char* p)
{
	int i = 0;
	int j = 0;
	int sLen = strlen(s);
	int pLen = strlen(p);
	while (i < sLen && j < pLen)
	{
		//如果j = -1，或者当前字符匹配成功（即S[i] == P[j]），都令i++，j++    
		if (j == -1 || s[i] == p[j])
		{
			i++;
			j++;
		}
		else
		{
			//如果j != -1，且当前字符匹配失败（即S[i] != P[j]），则令 i 不变，j = next[j]    
			//next[j]即为j所对应的next值      
			j = next[j];
		}
	}
	if (j == pLen)
		return i - j;
	else
		return -1;
}
```



> [参考自July](https://blog.csdn.net/v_july_v/article/details/7041827)
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        m={k:v for k,v in knowledge}
        w=re.split(r'[()]',s)
        out=[]
        for i ,w in enumerate(w):
            out.append(w if i%2==0 else m.get(w,"?"))
        return "".join(out)
def preorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        
        stk=[]
        pre=[]
        stk.append(root)
        left=[]
        right=[]
        
        while len(stk)>0:
            top= stk[len(stk)-1]
            
            pre.append(top.val)
            stk.pop()
            
            if len(top.children)>0:
                for i in range(len(top.children)-1,0,-1):
                    if top.children[i]!=None:
                        stk.append(top.children[i])
                
                if top.children[0]!=None:
                    stk.append(top.children[0])
        
       
        return pre

def preorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        
        pre=[]
        pre.append(root.val)
        left=[]
        right=[]
        
        for i in range(len(root.children)):
            if i==0:
                left= self.preorder(root.children[i])
            else:
                right+= self.preorder(root.children[i])
        
        pre+= left
        pre+= right
        return pre
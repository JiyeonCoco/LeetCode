class Solution:
    def simplifyPath(self, path: str) -> str:
        
        split_path = path.split('/')
        out_path = []

        for s in split_path:

            if (s == '.' or '/' in s or s == ''):
                continue
            elif s == '..':
                if out_path:
                    out_path.pop()
            else:
                out_path.append(s)

        return '/' + '/'.join(out_path)

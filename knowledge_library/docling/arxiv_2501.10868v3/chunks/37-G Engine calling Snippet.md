## G Engine calling Snippet

We provide a snippet of the engine code used in our experiments. The generation method of each engine has two main components: ' compile \_ grammar ' and ' call \_ engine '.

110

Guidance

48

41

Llamacpp

20

51

```
import time import stopit class BaseModel : @stopit.threading _ timeoutable(timeout=40) def compile _ grammar(self, json _ schema): status = "unknown" try : compiled _ grammar = self. _ compile _ grammar(json _ schema) status = "success" except Exception as e: # Any exception in this block will be caught and considered as schema not supported ↪ → compiled _ grammar = None status = "schema _ not _ supported" return compiled _ grammar, status def generate(self, prompt, json _ schema= None ): compile _ start _ time = time.time() compiled _ grammar = self.compile _ grammar(json _ schema) compile _ end _ time = time.time() # GCT (Grammar Compilation Time) gct = compile _ end _ time -compile _ start _ time gen _ start _ time = time.time() output, first _ tok _ arr _ time = self. _ call _ engine(prompt, compiled _ grammar) ↪ → # TTFT (Time to First Token) ttft = first _ tok _ arr _ time -gen _ start _ time gen _ end _ time = time.time() # TGT (Total Generation Time) tgt = gen _ end _ time -gen _ start _ time return output, gct, ttft, tgt def _ call _ engine(self, prompt, compiled _ grammar): raise NotImplementedError
```

Listing 9: Abstract BaseModel interface defining the calling of structured generation, including grammar compilation and text generation timing metrics.

We use the Listing 10 to validate the generated JSONs against the schema. The validation is done by the jsonschema library with format checking enabled.

We provide a snippet of how the engines are called in our experiments in Listings 11, 12, 13, and 14.

```
import jsonschema from jsonschema import Draft202012Validator, FormatChecker, ValidationError ↪ → format _ checker = FormatChecker() def is _ json _ schema _ valid(schema: dict): try : jsonschema.Draft202012Validator.check _ schema(schema) return True except jsonschema.SchemaError as e: return False def validate _ json _ against _ schema(json _ obj, json _ schema): if not is _ json _ schema _ valid(json _ schema): raise ValidationError("The JSON schema is invalid.") validator = Draft202012Validator(json _ schema, format _ checker=format _ checker) ↪ → return validator.validate(json _ obj)
```

Listing 10: Validation of the generated JSONs against the schema.

```
import guidance class GuidanceModel (BaseModel): def compile _ grammar(self, json _ schema): return guidance.json( schema=json _ schema, ) def _ call _ engine(self, prompt, compiled _ grammar): generator = self.guidance _ model.stream() + prompt + compiled _ grammar ↪ → for i, state in enumerate(generator): if i == 0: first _ state _ arr _ time = time.time() output = state return output, first _ state _ arr _ time
```

Listing 11: Invocation of the guidance engine.

```
import llama _ cpp class LlamaCppModel (BaseModel): def compile _ grammar(self, json _ schema): return ↪ → def _ call _ engine(self, prompt, compiled _ grammar): generator = self.llama _ cpp _ model.create _ chat _ completion(prompt, grammar=compiled _ grammar, stream= True ) ↪ → output = "" for i, token in enumerate(generator): if i == 0: first _ tok _ arr _ time = time.time() output += token return output, first _ tok _ arr _ time
```

Listing 13: Invocation of the Outlines engine.

```
llama _ cpp.llama _ grammar.LlamaGrammar.from _ json _ schema(json _ schema) Listing 12: Invocation of the LlamaCpp engine. import outlines class OutlinesModel (BaseModel): def compile _ grammar(self, json _ schema): return outlines.generate.json( schema _ object=json _ schema ) def _ call _ engine(self, prompt, compiled _ grammar): generator = self.generator.stream(prompt) output = "" for i, token in enumerate(generator): if i == 0: first _ tok _ arr _ time = time.time() output += token return output, first _ tok _ arr _ time
```

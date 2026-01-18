## import xgrammar

```
class TimingLogitsProcessor (LogitsProcessor): def __ init __ (self): super(). __ init __ () self.timestamps = [] def __ call __ (self, input _ ids, scores): current _ time = time.time() self.timestamps.append(current _ time) return scores class XGrammarModel (BaseModel): def compile _ grammar(self, json _ schema): return xgrammar.GrammarCompiler().compile _ json _ schema(json _ schema) ↪ → def _ call _ engine(self, prompt, compiled _ grammar): output = self.hf _ model.generate(prompt, logits _ processor=[compiled _ grammar, timeit _ logit _ processor]) ↪ → first _ tok _ arr _ time = timeit _ logit _ processor.timestamps[0] return output, first _ tok _ arr _ time
```

Listing 14: Invocation of the XGrammar engine.

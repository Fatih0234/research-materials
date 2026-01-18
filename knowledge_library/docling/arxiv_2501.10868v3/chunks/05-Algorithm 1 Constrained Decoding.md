## Algorithm 1 Constrained Decoding

```
Require: Constraint C , LLM f , Prompt x Ensure: Output o adhering to C 1: o ← [] 2: loop 3: C. update ( o ) ▷ advance state of C 4: m ← C. mask () ▷ compute mask 5: v ← f ( x + o ) ▷ compute logits 6: v ′ ← m ⊙ v ′ 7: t ← decode ( α ′ ) ▷ sample 8: if t = EOS then 9: break 10: end if 11: o. append ( t ) 12: end loop 13: return o ▷ output
```

strained decoding with unconstrained LMs [Roy et al., 2024; Tang et al., 2024; Yao et al., 2023a], the studies to date fail to provide comparisons across different constrained decoding frameworks. The benchmarks employed have either narrowly focused on specific tasks or rely on formal-grammar-based artificial setups, that have unclear relevance to real-world use cases.

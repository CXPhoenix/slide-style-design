# Evidence parser correction

The initial finalizer rejected CT03 because its choice prompt used a colon rather
than a question mark. The approved behavior requires a choice question, not fixed
punctuation. Manual review confirmed an explicit one-primary choice prompt; the
parser accepted that form. No product change or model rerun resulted. A surplus
EOF blank line was removed; final-route-check.log verifies that unchanged behavior.

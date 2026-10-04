# TDD

One integrity check failed because release-manifest.json did not exist. Minimal
delivery manifest now links every AC and checks candidate product/reply hashes;
green-01 passed. Manual meaning/source/revision review is separately documented.
At cycle 1, no product instructions changed; existing actual cases remained versioned. Cycle 2 below adds the narrow Gates acceptance correction.

Second cycle: independent semantic review invalidated T13 CT04 false pass; release
integrity test red-02 rejects the failed referenced case. Minimal Gates acceptance
clarification plus one affected actual case on new revision then supports revised
manifest, green-02. The static test detects invalid evidence, not LLM compliance.

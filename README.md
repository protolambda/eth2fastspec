# `eth2fastspec`

[![](https://img.shields.io/pypi/l/eth2fastspec.svg)](https://pypi.python.org/pypi/eth2fastspec) [![](https://img.shields.io/pypi/pyversions/eth2fastspec.svg)](https://pypi.python.org/pypi/eth2fastspec) [![](https://img.shields.io/pypi/status/eth2fastspec.svg)](https://pypi.python.org/pypi/eth2fastspec) [![](https://img.shields.io/pypi/implementation/eth2fastspec.svg)](https://pypi.python.org/pypi/eth2fastspec)


Eth2fastspec is an extension to [`eth2spec`](https://pypi.org/project/eth2spec/), utilizing the same types, configuration and dependencies, but optimized for transition speed.

## Usage

A few new objects are introduced for precomputed data, speeding up the transition:
- `ShufflingEpoch`: Committee shuffling information for a single epoch
- `EpochsContext`: A collection of contextual information to re-use during an epoch, and rotating precomputed data of the next epoch into the current epoch. This includes shuffling, but also proposer information is available.
    - `epochs_ctx.load_state(state)` precomputes the data for the given state.
    - `sync_pubkeys()` checks the precomputed data against a state, and then adds missing  pubkeys (strictly append-only however, not meant to fork this information)
    - `copy()` if a fork occurs, the context will have to be copied. To avoid copying the immutable parts, the `copy()` implements a specialized copy routine.
    - `rotate_epochs()` to re-use information, such as the shuffling of the next epoch, after transitioning into a new epoch, the `rotate_epochs()` is called. The transition function takes care of epoch-context data rotation.
- `FlatValidator`: A copy of the regular `Validator`, but in a simple object instead of a tree-representation. For intermediate computation the remerkleable representation slows things down, so a regular object is used instead.
- `AttesterStatus`: During the epoch transition, additional data is precomputed to avoid traversing any state a second time. Attestations are a big part of this, and each validator has an "status" to represent its precomputed participation.
- `EpochProcess`: The `AttesterStatus` (and `FlatValidator` under `status.validator`) objects and `EpochStakeSummary` are tracked in the `EpochProcess` and made available as additional context in the epoch transition.
    - `prepare_epoch_process_state(epochs_ctx, state)` computes this data.

Method signatures in the spec changed to utilize precomputed data:
 - `state_transition`, `process_slots`, `process_slot`, `process_epoch`, every epoch sub-process, `process_block`, every block sub-process, and `verify_block_signature` all have an additional `epochs_ctx` (`EpochsContext`) argument.
 - every epoch sub-process has an additional `process` (`EpochProcess`) argument.
 
 The argument order is generally: `epochs_ctx`, `proces`, `state`, remaining args.

 ```python

from eth2spec.config.config_util import prepare_config
# Example: load a config, loading it in `eth2spec` as well as `eth2fastspec`, before loading the spec modules.
prepare_config("./lighthouse", "config")

import eth2fastspec as spec

state: spec.BeaconState = ...  # BeaconState.deserialize(stream, size), or some other source.
block: spec.SignedBeaconBlock = ...

epochs_ctx = spec.EpochsContext()
epochs_ctx.load_state(state)

spec.state_transition(epochs_ctx, state, block)

print(state.hash_tree_root().hex())
```

## License

MIT, see [LICENSE](./LICENSE) file.

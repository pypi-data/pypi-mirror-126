#!/bin/bash

set -eux

export PATH=$PATH:/builds/worker/clang/bin
export ORG_GRADLE_PROJECT_RUST_ANDROID_GRADLE_TARGET_X86_64_APPLE_DARWIN_CC=/builds/worker/clang/bin/clang
export ORG_GRADLE_PROJECT_RUST_ANDROID_GRADLE_TARGET_X86_64_APPLE_DARWIN_TOOLCHAIN_PREFIX=/builds/worker/cctools/bin
export ORG_GRADLE_PROJECT_RUST_ANDROID_GRADLE_TARGET_X86_64_APPLE_DARWIN_AR=/builds/worker/cctools/bin/x86_64-apple-darwin-ar
export ORG_GRADLE_PROJECT_RUST_ANDROID_GRADLE_TARGET_X86_64_APPLE_DARWIN_RANLIB=/builds/worker/cctools/bin/x86_64-apple-darwin-ranlib
export ORG_GRADLE_PROJECT_RUST_ANDROID_GRADLE_TARGET_X86_64_APPLE_DARWIN_LD_LIBRARY_PATH=/builds/worker/clang/lib
export ORG_GRADLE_PROJECT_RUST_ANDROID_GRADLE_TARGET_X86_64_APPLE_DARWIN_RUSTFLAGS="-C linker=/builds/worker/clang/bin/clang -C link-arg=-B -C link-arg=/builds/worker/cctools/bin -C link-arg=-target -C link-arg=x86_64-apple-darwin -C link-arg=-isysroot -C link-arg=/tmp/MacOSX10.12.sdk -C link-arg=-Wl,-syslibroot,/tmp/MacOSX10.12.sdk -C link-arg=-Wl,-dead_strip"
# For ring's use of `cc`.
export ORG_GRADLE_PROJECT_RUST_ANDROID_GRADLE_TARGET_X86_64_APPLE_DARWIN_CFLAGS_x86_64_apple_darwin="-B /builds/worker/cctools/bin -target x86_64-apple-darwin -isysroot /tmp/MacOSX10.12.sdk -Wl,-syslibroot,/tmp/MacOSX10.12.sdk -Wl,-dead_strip"
# The wrong linker gets used otherwise: https://github.com/rust-lang/rust/issues/33465.
export ORG_GRADLE_PROJECT_RUST_ANDROID_GRADLE_TARGET_X86_64_PC_WINDOWS_GNU_RUSTFLAGS="-C linker=x86_64-w64-mingw32-gcc"

# Ensure we're compiling dependencies in non-debug mode.
# This is required for rkv/lmdb to work correctly on Android targets and not link to unavailable symbols.
export TARGET_CFLAGS="-DNDEBUG"

# Install clang, a port of cctools, and the macOS SDK into /tmp.
# If it weren't for the size we could do it in the Dockerfile directly to cache it.
#
# To update:
# * Go to https://firefox-ci-tc.services.mozilla.com/tasks/index/gecko.cache.level-3.toolchains.v3
# * Find the tasks for `linux64-clang-11-macosx-cross` and `linux64-cctools-port-clang-11` (or higher Clang version)
# * Per task, follow the link to the latest indexed task
# * In the detail view, click "View Task"
# * In the task view, click "See more"
# * Find the "Routes" list
# * Pick the "index.*.hash.*" route
# * Use that in the URLs below
#   (drop the "index." prefix, ensure the "public/build" path matches the artifacts of the TC task)
pushd /builds/worker
curl -sfSL --retry 5 --retry-delay 10 \
    https://firefox-ci-tc.services.mozilla.com/api/index/v1/task/gecko.cache.level-3.toolchains.v3.linux64-cctools-port-clang-11.hash.0605c7bc8e4a474ee8ffa6d9e075f57d5063ff31793516d9f62dc6e7dcec41c3/artifacts/public/build/cctools.tar.xz > cctools.tar.xz && \
tar -xf cctools.tar.xz && \
rm cctools.tar.xz && \
curl -sfSL --retry 5 --retry-delay 10 \
    https://firefox-ci-tc.services.mozilla.com/api/index/v1/task/gecko.cache.level-3.toolchains.v3.linux64-clang-11-macosx-cross.hash.8da28431c601f847cd59f8582181836e1acbb263c434cb6151d361d835812afb/artifacts/public/build/clang.tar.zst > clang.tar.zst && \
tar -I zstd -xf clang.tar.zst && \
rm clang.tar.zst
popd

pushd /tmp

tooltool.py \
  --url=http://taskcluster/tooltool.mozilla-releng.net/ \
  --manifest="/builds/worker/checkouts/src/taskcluster/scripts/macos.manifest" \
  fetch

rustup target add x86_64-apple-darwin
rustup target add x86_64-pc-windows-gnu

popd

set +eux

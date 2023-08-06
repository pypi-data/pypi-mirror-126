charmonium.async_subprocess
===========================

See the documentation of the main function::

   async def run(
       args: Sequence[StrBytes],
       cwd: Optional[Path] = None,
       env: Optional[Union[Mapping[StrBytes, StrBytes]]] = None,
       env_override: Optional[Mapping[StrBytes, StrBytes]] = None,
       capture_output: bool = False,
       check: bool = False,
       text: Optional[bool] = None,
   ) -> subprocess.CompletedProcess:
       """An async clone of `subprocess.run`.
   
       Suppose you have Python script that orchestrates shell commands,
       but it's too slow, and you've identified commands which can run in
       parallel. You could use `threading`, but that has GIL problems, or
       `multiprocess`, which has a high startup-cost per worker. You are
       already spinning off subprocesses, which the OS will run
       concurrently, so why not use async/await programming to express
       concurrency in a single thread?
   
       Note this function does not permit you to communicate
       asynchronously, just to run commands asynchronously.
   
       This function supports a subset of the signature of
       `subprocess.run`, that I will expand based on need. If you need
       some functionality, submit an issue or PR.
   
       """

{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { flake-utils, nixpkgs, ... }: 
  flake-utils.lib.eachDefaultSystem (system: let
    pkgs = import nixpkgs { inherit system; };
  in {
    devShell = pkgs.mkShell {
      buildInputs = with pkgs.python312Packages; [
        pkgs.python312
        pip
        requests
        tqdm
      ];

      shellHook = ''
        PS1="(kattis)\n$PS1"
      '';
    };
  });
}

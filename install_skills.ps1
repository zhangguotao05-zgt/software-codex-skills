[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$DestinationRoot = (Join-Path $env:USERPROFILE '.agents\skills')
)

$ErrorActionPreference = 'Stop'
$skillName = 'software-development'
$sourcePath = Join-Path $PSScriptRoot "skills\$skillName"
$destinationPath = [IO.Path]::GetFullPath((Join-Path $DestinationRoot $skillName))

if (-not (Test-Path -LiteralPath (Join-Path $sourcePath 'SKILL.md') -PathType Leaf)) {
    throw 'The source skill is incomplete.'
}
if (Test-Path -LiteralPath $destinationPath) {
    throw "The destination already exists; preserve and review local changes first: $destinationPath"
}
if ($destinationPath.StartsWith(
    [IO.Path]::GetFullPath($PSScriptRoot) + [IO.Path]::DirectorySeparatorChar,
    [StringComparison]::OrdinalIgnoreCase
)) {
    throw 'Install outside the source repository.'
}

if ($PSCmdlet.ShouldProcess($destinationPath, 'Install the software-development skill')) {
    New-Item -ItemType Directory -Path ([IO.Path]::GetDirectoryName($destinationPath)) -Force | Out-Null
    Copy-Item -LiteralPath $sourcePath -Destination $destinationPath -Recurse -ErrorAction Stop
    Write-Output "Installed $skillName. It will be available in the next Codex turn."
}

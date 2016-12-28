Plan
----
1. Basic single TI-Bear sprite.
2. 'Drop' the TI-Bear sprite down the screen.
3. Have a landing pad area and a lava area. Bears can rest on pad and die on
   lava.
4. Drop multiple bears. Have them stack.
5. Add center of mass/gravity
    + Add visualisation of COM
    + Add visualisation of Topple point
    + Add visualisation of "if a Bear would topple/is unstable"
6. Add rotation of simple Bear sprite.
    + so no AABBs, aside from collision broad-phase.
    + separate test app (or test mode) with appropriate visuals
    + left/right + shift,ctrl,alt etc, and allow typing in +/- degrees + enter
7. Rotate bear around another point
    + i.e. a bears centre of mass
8. Add Bear-parts
    + Add centre-of-gravity for entire bear/bear-parts
    + Topple points
    + Bear parts rotate when Bear rotates

Backlog
-------
+ Mouse interface
+ Ability to pin balloons to bear-parts to make them lighter
    + Balloons are in a separate "layer" and other bears can just pass through 
      them.

Canned ideas
------
+ Better physics?
    + For BTT 2.0
    + Add bounce when a bear drops? 
    + Squidgeyness/compressability.
        + bulk modulus? strength of materials? elasticity??
        + density that changes over the course of the game
            + density is specific to the volume,
            + so a squished bear is more dense.
    + Ramps at the base of the tower?
    + bean-bag filled bears?
+ Expanding bears that slowly grow outwards, putting more pressure into the 
  situation?
+ Bears with helium balloons attached?
    + Or the player can attach a balloon to any
      bear-part, with a limited number of balloons?
    + The bear exerts less pressure, but the balloon is at risk of being popped
    + Balloon will just be bear-parts?
+ Can 'vacuum-pack' some bears to make them more dense
+ Bears can be penetrated?
    + Bed of nails?
    + Razor thing bears
    + Penetrated bears (stuffing) are now pinned to the other part??
    + Inflated bears (helium/air) are popped?


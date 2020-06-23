class  GamePad extends UIBlock {
    constructor(config)
    {
        super();
        this.scene=config.scene;
        this.grid=config.grid;

        this.scene.add.image(0,0,'cross'); 
    }
}
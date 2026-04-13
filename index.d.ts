declare module 'esptk' {
  class ESPFile {
    constructor(filePath: string, gameMode: string);
    setLightFlag(enabled: boolean): void;
    isMaster: boolean;
    isMedium: boolean;
    isLight: boolean;
    isBlueprint: boolean;
    isDummy: boolean;
    author: string;
    description: string;
    masterList: string[];
    revision: number;
  }
  export default ESPFile;
}

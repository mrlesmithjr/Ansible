BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "AnsiblePlaybooks" (
	`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Description` TEXT,
	`Path` TEXT,
	UNIQUE (Name,Path)
);
CREATE TABLE IF NOT EXISTS "Hosts" (
	`HostId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`HostName`	TEXT NOT NULL UNIQUE,
	`HostDescription`	TEXT,
	`HostCreatedOn`	TEXT,
	`LastUpdateTime`	TEXT
);
CREATE TABLE IF NOT EXISTS "HostDetails" (
	`HostDetailsId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`HostArchitecture`	TEXT,
	`HostBIOSDate`	TEXT,
	`HostBIOSVersion`	TEXT,
	`HostDistribution`	TEXT,
	`HostDistributionRelease`	TEXT,
	`HostDistributionVersion`	TEXT,
	`HostFQDN`	TEXT,
	`HostHardDrive`	TEXT,
	`HostHardDrivePartions`	TEXT,
	`HostHardDriveSize`	TEXT,
	`HostInterface`	TEXT,
	`HostInterfaceAddress`	TEXT,
	`HostInterfaceGateway`	TEXT,
	`HostInterfaceMAC`	TEXT,
	`HostInterfaceNetmask`	TEXT,
	`HostInterfaces`	TEXT,
	`HostKernel`	TEXT,
	`HostMemFreeMB`	INTEGER,
	`HostMemTotalMB`	INTEGER,
	`HostMounts`	TEXT,
	`HostOSFamily`	TEXT,
	`HostProcessor`	TEXT,
	`HostProcessorCores`	INTEGER,
	`HostProcessorCount`	INTEGER,
	`HostProductName`	TEXT,
	`HostSwapFree`	INTEGER,
	`HostSwapTotal`	INTEGER,
	`HostSystemVendor`	TEXT,
	`HostTimeZone`	TEXT,
	`HostVirtualizationType`	TEXT,
	`LastUpdateTime`	TEXT,
	`HostId`	INTEGER,
	FOREIGN KEY(`HostId`) REFERENCES Hosts ( HostId ) ON DELETE CASCADE ON UPDATE CASCADE,
	UNIQUE (HostId,HostFQDN)
);
CREATE TABLE IF NOT EXISTS "Groups" (
	`GroupId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`GroupName`	TEXT NOT NULL UNIQUE,
	`GroupDescription`	TEXT,
	`GroupDTAP`	CHAR(1) NOT NULL,
	`GroupCreatedOn`	TEXT,
	`LastUpdateTime`	TEXT
);
CREATE TABLE IF NOT EXISTS "GroupVars" (
	`VarsId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`VarName`	TEXT NOT NULL UNIQUE,
	`VarDescription`	TEXT,
	`VarReference`	TEXT NOT NULL,
	`VarSet`	TEXT NOT NULL,
	`VarValue`	TEXT NOT NULL,
	`LastUpdateTime`	TEXT,
	`GroupId`	INTEGER NOT NULL,
	FOREIGN KEY(`GroupId`) REFERENCES Groups ( GroupId ) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "GroupContact" (
	`ContactId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`ContactName`	TEXT NOT NULL,
	`ContactEmail`	TEXT NOT NULL,
	`ContactPhone`	TEXT NOT NULL,
	`ContactCreatedOn`	TEXT,
	`LastUpdateTime`	TEXT,
	`GroupId`	INTEGER NOT NULL,
	FOREIGN KEY(`GroupId`) REFERENCES Groups ( GroupId ) ON DELETE CASCADE ON UPDATE CASCADE,
	UNIQUE (ContactName,ContactEmail)
);
CREATE TABLE IF NOT EXISTS "HostGroups" (
	`HostGroupId`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`GroupId`	INTEGER NOT NULL,
	`GroupName` TEXT NOT NULL,
	`HostId`	INTEGER NOT NULL,
	`HostName` TEXT NOT NULL,
	FOREIGN KEY(`GroupId`) REFERENCES Groups (GroupId) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(`HostId`) REFERENCES Hosts ( HostId ) ON DELETE CASCADE ON UPDATE CASCADE,
  UNIQUE (GroupId,HostId)
);
CREATE TABLE IF NOT EXISTS "LoginAttempts" (
	`Id` INTEGER PRIMARY KEY AUTOINCREMENT,
	`UserId` INTEGER NOT NULL,
	`Time` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "Users" (
	`UserId` INTEGER PRIMARY KEY AUTOINCREMENT,
	`Email` TEXT NOT NULL,
	`FirstName` TEXT NOT NULL,
	`LastName` TEXT NOT NULL,
	`Password` CHAR(128) NOT NULL,
	`Phone` TEXT,
	`Role` TEXT NOT NULL DEFAULT 'user',
	`Salt` CHAR(128),
	`UserName` TEXT NOT NULL,
	UNIQUE (UserName,Email)
);
CREATE TABLE IF NOT EXISTS "UsersExtAPILinks" (
	`Id` INTEGER PRIMARY KEY AUTOINCREMENT,
	`APIToken` TEXT,
	`JenkinsURL` TEXT,
	`JenkinsAPITokenUserId` TEXT,
	`JenkinsUserAPIToken` TEXT,
	`Name` TEXT,
	`Url` TEXT,
	`UserId` INTEGER NOT NULL,
	FOREIGN KEY ('UserId') REFERENCES Users (UserId) ON DELETE CASCADE ON UPDATE CASCADE,
	UNIQUE (UserId,Name,Url,APIToken),
	UNIQUE (UserId,JenkinsURL,JenkinsAPITokenUserId,JenkinsUserAPIToken)
);
CREATE TABLE IF NOT EXISTS "UsersLinks" (
	`Id` INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name` TEXT NOT NULL,
	`Url` TEXT NOT NULL,
	`UserId` INTEGER NOT NULL,
	FOREIGN KEY(`UserId`) REFERENCES Users (UserId) ON DELETE CASCADE ON UPDATE CASCADE,
	UNIQUE (UserId,Name,Url)
);
CREATE TABLE IF NOT EXISTS "GroupContactLog" (
	`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`OldContactName`	TEXT,
	`NewContactName`	TEXT,
	`OldContactEmail`	TEXT,
	`NewContactEmail`	TEXT,
	`OldContactPhone`	TEXT,
	`NewContactPhone`	TEXT,
	`Date`	TEXT
);
CREATE TABLE IF NOT EXISTS "GroupVarsLog" (
	`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`OldVarName`	TEXT,
	`NewVarName`	TEXT,
	`OldVarDescription`	TEXT,
	`NewVarDescription`	TEXT,
	`OldVarReference`	TEXT,
	`NewVarReference`	TEXT,
	`OldVarSet`	TEXT,
	`NewVarSet`	TEXT,
	`OldVarValue`	TEXT,
	`NewVarValue`	TEXT,
	`Date`	TEXT
);
CREATE TABLE IF NOT EXISTS "GroupsLog" (
	`Id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`OldGroupName`	TEXT,
	`NewGroupName`	TEXT,
	`OldGroupDescription`	TEXT,
	`NewGroupDescription`	TEXT,
	`Date`	TEXT
);
CREATE TRIGGER IF NOT EXISTS GroupContactUpdated UPDATE OF ContactName ON GroupContact
BEGIN
INSERT INTO GroupContactLog(OldContactName, NewContactName, Date) VALUES (old.ContactName, New.ContactName, datetime('now'));
END;
COMMIT;
